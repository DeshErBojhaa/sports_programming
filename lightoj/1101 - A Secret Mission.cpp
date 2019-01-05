#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<string.h>
#include<iostream>

using namespace std;

struct data
{
    int from,to,cost;
};
data tmp;

struct DATA
{
    int to,cost;
};
DATA TMP;

vector<DATA>adj[50001];
vector<data>vec;
int node,con,parent[50001],rank[50001],level[50001],ancestor[50001][17],dyst[50001][17],durotto[50001];


/// ************************ MST PART **************************** ///

bool comp(data a,data b)
{
    return a.cost<b.cost;
}

void make_parent()
{
    for(int i=1; i<=node; i++)
    {
        parent[i]=i;
        rank[i]=0;
    }
    return;
}

int fp(int a)
{
    if(parent[a]!=a) return fp(parent[a]);
    else return a;
}

void join(int a,int b)
{
    if(rank[a]>rank[b]) parent[b]=a;
    else
    {
        parent[a]=b;
        if(rank[a]==rank[b]) rank[b]++;
    }
    return;
}

void mst()
{
    make_parent();

    for(int i=0; i<vec.size(); i++)
    {
        int from=vec[i].from;
        int to=vec[i].to;
        int cost=vec[i].cost;

        if(fp(from)!=fp(to))
        {
            join(fp(from),fp(to));

            TMP.to=to;
            TMP.cost=cost;

            adj[from].push_back(TMP);
            TMP.to=from;
            adj[to].push_back(TMP);
        }
    }

    return;
}

/// ******************************** MST PART ****************************///

void dfs(int cur,int par,int lev)
{
    parent[cur]=par;
    level[cur]=lev;

    for(int i=0; i<adj[cur].size(); i++)
    {
        int to=adj[cur][i].to;
        int cost=adj[cur][i].cost;

        if(level[to]==-1)
        {
            durotto[to]=cost;
            dfs(to,cur,lev+1);
        }
    }
    return;
}



void lca_preprocess()
{
    memset(level,-1,sizeof level);

    for(int j=0; (1<<j) <=node; j++)
        for(int i=1; i<=node; i++)
        {
            dyst[i][j]=-(1<<28);
            ancestor[i][j]=-1;
        }

    dyst[1][0]=0;
    durotto[1]=0;
    dfs(1,1,0);

    for(int i=1; i<=node; i++)
    {
        ancestor[i][0]=parent[i];
        dyst[i][0]=durotto[i];
    }

    for(int j=1; (1<<j)< node; j++)
        for(int i=1; i<=node; i++)
        {
            int half_way=ancestor[i][j-1];
            if(half_way !=-1)
            {
                ancestor[i][j]=ancestor[ half_way ][j-1];
                dyst[i][j]=max( dyst[i][j] , max(dyst[i][j-1], dyst[half_way][j-1]) );
            }
        }
    return;
}

int Query(int P,int Q)
{
    int ans=-(1<<28);

    if(level[P]<level[Q])     swap(P,Q);

    int log=0;

    for(log=1; (1<<log)<=node; log++);
    log--;

    for(int i=log; i>=0; i--)
    {
        if(level[P]- (1<<i) >= level[Q])
        {
            ans=max(ans,dyst[P][i]);
            P=ancestor[P][i];
        }
    }

    if(P==Q)
        return ans;

    for(int i=log; i>=0; i--)
    {
        if(ancestor[P][i]!=-1 && ancestor[Q][i]!=-1 && ancestor[P][i]!=ancestor[Q][i])
        {
            ans=max(ans, max(dyst[P][i],dyst[Q][i]) );
            P=ancestor[P][i];
            Q=ancestor[Q][i];
        }
    }

    ans=max(ans,max(dyst[P][0],dyst[Q][0])  );
    return ans;
}

int main()
{
    int T,Q;
    scanf(" %d",&T);

    for(int tt=1; tt<=T; tt++)
    {
        vec.clear();
        scanf(" %d %d",&node,&con);
        for(int i=1; i<=node; i++) adj[i].clear();

        for(int i=0; i<con; i++)
        {
            int a,b,c;
            scanf(" %d %d %d",&a,&b,&c);

            tmp.from=a;
            tmp.to=b;
            tmp.cost=c;

            vec.push_back(tmp);
        }

        sort(vec.begin(),vec.end(),comp);

        mst();

        lca_preprocess();
        scanf(" %d",&Q);
        printf("Case %d:\n",tt);

        for(int i=0; i<Q; i++)
        {
            int ff,tt;
            scanf(" %d %d",&ff,&tt);
            int ans=Query(ff,tt);
            if(ff==tt) ans=0;
            printf("%d\n",ans);
        }
    }

    return 0;
}

/*
3
8 13
1 2 10
1 3 100
2 4 99
3 4 99
4 5 10
5 6 200
5 7 10
6 8 20
7 8 30
1 4 100
2 3 100
6 7 1
5 8 50

*/
