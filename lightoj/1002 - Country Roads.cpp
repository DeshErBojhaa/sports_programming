#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<iostream>

using namespace std;

struct data
{
    int f,t,w;
};

int n,con,home,node[501],rank[501],cost[505],parent[505];
vector<data> V;


bool com(data a,data b)
{
    return a.w<b.w;
}

void make_parent(int node)
{
    parent[node]=node;
    rank[node]=0;
    return;
}

int find_parent(int node)
{
    if(node!=parent[node]) return parent[node]=find_parent(parent[node]);
    return parent[node];
}

void join(int a,int b)
{
    if(rank[a]>rank[b]) parent[b]=a;
    else
    {
        parent[b]=a;
        if(rank[a]==rank[b]) rank[b]++;
    }
    return;
}

void mst(void)
{
    for(int i=0;i<n;i++)
       make_parent(i);

    for(int i=0;i<V.size();i++)
    {
        int from=V[i].f;
        int to=V[i].t;
        int weight=V[i].w;

        if(find_parent(from)!=find_parent(to))
        {
            join(find_parent(from),find_parent(to));
            {
                for(int j=0;j<n;j++)
                {
                    if(find_parent(home)==find_parent(j) && cost[j]==-1)
                    {
                        cost[j]=weight;
                    }
                }
            }
        }
    }
    return;
}

int main()
{
    int tc;
    scanf(" %d",&tc);
    for(int tt=1;tt<=tc;tt++)
    {
        scanf(" %d %d",&n,&con);
        for(int i=0;i<con;i++)
        {
            int ff,tt,ww;
            data tmp;
            scanf(" %d %d %d",&ff,&tt,&ww);
            tmp.f=ff; tmp.t=tt; tmp.w=ww;
            V.push_back(tmp);
        }
        scanf(" %d",&home);

        memset(cost,-1,sizeof cost);
        sort(V.begin(),V.end(),com);
        mst();
        cost[home]=0;

        printf("Case %d:\n",tt);
        for(int i=0;i<n;i++)
        {
           if(cost[i]!=-1) printf("%d\n",cost[i]);
           else printf("Impossible\n");
        }
        V.clear();
    }
    return 0;
}
