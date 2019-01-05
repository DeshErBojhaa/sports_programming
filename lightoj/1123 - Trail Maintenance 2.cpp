#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>

using namespace std;

struct data
{
    int from,to,cost;
};


vector<data>V;                  /// input
vector<data>use;               /// now hisebe
//vector<data>puchut;
//vector<int>ans;

int node,con,par[202],rank[202],Count;
int tmp_cost=0;

data make_struct(int f,int t,int c)
{
    data tmp;
    tmp.from=f;
    tmp.to=t;
    tmp.cost=c;

    return tmp;
}

bool bom(data a,data b)
{
    return a.cost<b.cost;
}

void make_set()
{
    for(int i=1; i<=node; i++)
    {
        par[i]=i;
        rank[i]=0;
    }
    return ;
}

int find_parent(int a)
{
    if(par[a]!=a) return par[a]=find_parent(par[a]);
    else return a;
}

void join(int a,int b)
{
    if(rank[a]>rank[b]) par[b]=a;
    else
    {
        par[a]=b;
        if(rank[a]==rank[b]) rank[b]++;
    }
    return;
}

void mst()
{
    make_set();

    for(int i=0; i<use.size(); i++)
    {
        if(Count==node-1) {use=V;return;}
        int ff,tt,cc;

        ff=use[i].from;
        tt=use[i].to;
        cc=use[i].cost;

        if(find_parent(ff)!=find_parent(tt))
        {
            join(find_parent(ff),find_parent(tt));
            tmp_cost+=cc;
            Count++;
            V.push_back(use[i]);
        }

    }
    use=V;
    return;
}

int main()
{
    int T,f,t,c;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        use.clear();

        Count=0;
        tmp_cost=0;

        scanf(" %d %d",&node,&con);
        printf("Case %d:\n",tt);
        for(int i=1; i<=con; i++)
        {
            V.clear();
            Count=0; tmp_cost=0;
            scanf(" %d %d %d",&f,&t,&c);
            use.push_back(make_struct(f,t,c));
            sort(use.begin(),use.end(),bom);
            mst();
            if(Count<node-1) printf("-1\n");
            else printf("%d\n",tmp_cost);

        }
    }
    return 0;
}
