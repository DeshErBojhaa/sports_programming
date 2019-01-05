#include<stdio.h>
#include<algorithm>
#include<string>
#include<math.h>
#include<iostream>
#include<vector>
#include<queue>
#include<string.h>
#include<map>

using namespace std;

struct data
{
    int from, to, cost;
};

map<string,int> mp;
vector<data>V;
int rank[100],parent[100];

bool com(data a, data b)
{
    return a.cost<b.cost;
}

void make_parent(int node)
{
    parent[node]=node;
    rank[node]=0;
    return;
}

int find_parent(int node)
{
    if(parent[node]!=node) return find_parent(parent[node]);
    return parent[node];
}

void join(int u,int v)
{
    if(rank[u]>rank[v]) parent[v]=u;
    else parent[u]=v;

    if(rank[u]==rank[v]) rank[v]++;

    return;
}

int mst(int sz)
{
    for(int i=1; i<=sz; i++) make_parent(i);
    int ans=0;

    for(int i=0; i<V.size(); i++)
    {
        int u=V[i].from;
        int v=V[i].to;
        int cst=V[i].cost;

        if(find_parent(u)!=find_parent(v))
        {
            join(find_parent(u),find_parent(v));
            ans+=cst;
        }
    }

    for(int i=1; i<sz; i++)
        for(int j=1; j<sz; j++)
            if(find_parent(i)!=find_parent(j)) return -1;
    return ans;
}

int main()
{
    int tc,w;
    scanf(" %d",&tc);

    for(int tt=1; tt<=tc; tt++)
    {
        mp.clear();
        V.clear();
        memset(rank,0,sizeof rank);
        memset(parent,0,sizeof parent);

        int con,ind=1;
        scanf(" %d",&con);

        for(int i=0; i<con; i++)
        {
            string str1,str2;
            cin>> str1>> str2;
            scanf(" %d",&w);

            if(mp[str1]==0)
            {
                mp[str1]=ind;
                ind++;
            }
            if(mp[str2]==0)
            {
                mp[str2]=ind;
                ind++;
            }

            data tmp;
            tmp.from=mp[str1];
            tmp.to=mp[str2];
            tmp.cost=w;

            V.push_back(tmp);
        }

        sort(V.begin(),V.end(),com);

        int ans=0;
        ans=mst(mp.size());
        if(ans==-1) printf("Case %d: Impossible\n",tt);
        else
        printf("Case %d: %d\n",tt,ans);

    }
    return 0;
}
