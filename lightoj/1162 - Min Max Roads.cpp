#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<string>
#include<vector>

using namespace std;

typedef pair<int,int> pii;

struct data
{
    int to,length;
};

vector<data>adj[100002];

pii dyst[100002][18];
int node,level[100002],ancestor[100002][18],parent[100002];

void dfs(int cur,int par,int lev)
{
    parent[cur]=par;
    level[cur]=lev;

    for(int i=0; i<adj[cur].size(); i++)
    {
        int to=adj[cur][i].to;
        int cost=adj[cur][i].length;

        if(parent[to]==-1)
        {
            dyst[to][0]=make_pair(cost,cost);
            dfs(to,cur,lev+1);
        }
    }
    return;
}

void pre_process()
{
    for(int j=0; (1<<j)<=node; j++)
        for(int i=0; i<=node; i++)
        {
            dyst[i][j]=make_pair(1<<28,0);
            ancestor[i][j]=-1;
        }

    dyst[1][0]=make_pair(0,0);  /// initialing dystence
    dfs(1,1,0);

    for(int i=1;i<=node;i++)
        ancestor[i][0]=parent[i];

    for(int j=1; (1<<j) < node ;j++)
    {
        for(int i=1;i<=node;i++)
        {
            int half_way=ancestor[i][j-1];
            if(half_way != -1)
            {
                ancestor[i][j]= ancestor[ half_way ][j-1];
                dyst[i][j]=make_pair(min(dyst[i][j-1].first, dyst[half_way][j-1].first)  ,  max(dyst[i][j-1].second, dyst[half_way][j-1].second));
            }
        }
    }

    return;
}

pii Query(int P,int Q)
{
    pii ans;
    ans=make_pair(1<<28,0);

    if(level[P]<level[Q]) swap(P,Q);

    int log=0;

    for(log=1;(1<<log)<node; log++); log--;

    for(int i=log;i>=0;i--)
        if(level[P]- (1<<i)  >=level[Q])
            {
                ans=make_pair(min(ans.first,dyst[P][i].first ), max(ans.second, dyst[P][i].second) );
                P=ancestor[P][i];
            }
    if(P==Q) return ans;   /// crossing this point

    for(int i=log;i>=0;i--)
    {
        if(ancestor[P][i] != -1 && ancestor[Q][i] != -1 && ancestor[P][i]!=ancestor[Q][i])
        {
            int a=min(dyst[P][i].first,dyst[Q][i].first);
            int b=max(dyst[P][i].second,dyst[Q][i].second);
            ans=make_pair(min(a,ans.first),max(b,ans.second));
            P=ancestor[P][i];
            Q=ancestor[Q][i];
        }
    }

    ans=make_pair(min(ans.first,min(dyst[P][0].first,dyst[Q][0].first)), max(ans.second, max(dyst[P][0].second,dyst[Q][0].second)) );

    return ans;

}

int main()
{
    int T;
    scanf(" %d",&T);

    for(int tt=1; tt<=T; tt++)
    {
        scanf(" %d",&node);
        memset(parent,-1,sizeof parent);

        for(int i=1; i<=node; i++) adj[i].clear();

        for(int i=1; i<node; i++)
        {
            int a,b,c;
            scanf(" %d %d %d",&a,&b,&c);
            data tmp;
            tmp.length=c;
            tmp.to=a;

            adj[b].push_back(tmp);

            tmp.to=b;
            adj[a].push_back(tmp);
        }

        pre_process();
        int query;
        scanf(" %d",&query);

        printf("Case %d:\n",tt);

        for(int qq=1;qq<=query;qq++)
        {
            int p,q;
            scanf(" %d %d",&p,&q);

            if(p==q)
            {
                printf("0 0\n"); continue;
            }
            pii ans=Query(p,q);

            printf("%d %d\n",ans.first,ans.second);

        }
    }
    return 0;
}
