#include<stdio.h>
#include<algorithm>
#include<queue>
#include<string>
#include<string.h>
#include<iostream>

using namespace std;

int junction,con,dys[200],col[200];

struct data
{
    int node,cost;
};

struct ver
{
    int node,cost;
    bool operator<(const ver & x)const
    {
        return cost>x.cost;
    }
};

vector<data> adj[110];

bool relax(int u,int v,int cost)
{
    if(dys[u]+cost<dys[v]) {dys[v]=dys[u]+cost; return true;}
    else return false;
}

int dijkstra(int source)
{
    priority_queue<ver> Q;

    for(int i=0;i<=junction;i++) col[i]=0;
    for(int i=0;i<=junction;i++) dys[i]=1<<30;
    dys[source]=0;

    ver tmp;
    tmp.cost=0; tmp.node=source;
    Q.push(tmp);

    while(!Q.empty())
    {
        tmp=Q.top(); Q.pop();
        int u=tmp.node;
        if(col[u]==0)
        {
            col[u]=1;
            for(int i=0;i<adj[u].size();i++)
            {
                int v=adj[u][i].node;
                int cst=adj[u][i].cost;

                if(relax(u,v,cst))
                {
                    tmp.cost=dys[v];
                    tmp.node=v;
                    Q.push(tmp);
                }
            }
        }
    }
    return dys[junction];
}

int main()
{
    int tc;
    scanf(" %d",& tc);
    for(int  tt=1;tt<=tc;tt++)
    {
        scanf(" %d %d",&junction,&con);
        for(int i=0;i<=junction;i++) adj[i].clear();  /// clear vector
        int f,t,c;

        for(int i=0;i<con;i++)
        {
            scanf(" %d %d %d",&f,&t,&c);
            data tmp;
            tmp.node=f;
            tmp.cost=c;
            adj[t].push_back(tmp);
            tmp.node=t;
            adj[f].push_back(tmp);
        }

        int ans=dijkstra(1);
        if(ans==1<<30)
        printf("Case %d: Impossible\n",tt);
        else
        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}
