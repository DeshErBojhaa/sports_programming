#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>
#include<vector>

using namespace std;

int total,invited;
long long ans;
bool flag[100009];

vector<int>adj[100009];

void dfs(int cur)
{
    invited++;
    flag[cur]=true;

    for(int i=0;i<adj[cur].size();i++)
    {
        int to=adj[cur][i];

        if(flag[to]==false)
        {
            dfs(to);
        }
    }

    ans+=total-invited;
    return;
}

int main()
{
    int T;
    scanf(" %d",&T);

    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d",&total);

        for(int i=0;i<=total;i++) adj[i].clear();
        ans=0,invited=0;
        memset(flag,false,sizeof flag);

        for(int i=0;i<total-1;i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            adj[a].push_back(b);
        }

        dfs(1);

        printf("Case %d: %d %lld\n",tt,total-1,ans);
    }
    return 0;
}
