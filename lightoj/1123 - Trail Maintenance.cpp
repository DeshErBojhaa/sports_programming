#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

struct data
{
    int from,to,cost;
};
data tmp;
int par[209],rank[209];


vector<data>v;

bool com(data a,data b)
{
    return a.cost<b.cost;
}

int fp(int a)
{
    if(par[a]!=a) return fp(par[a]);
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

int mst()
{
    int ans=0;
    for(int i=0; i<=101; i++)
    {
        par[i]=i;
        rank[i]=0;
    }

    for(int i=0; i<v.size(); i++)
    {
        int f,t,c;
        f=v[i].from;
        t=v[i].to;
        c=v[i].cost;
        if(fp(f)!=fp(t))
        {
            join(fp(f),fp(t));
            ans+=c;
        }
    }
    return ans;
}

