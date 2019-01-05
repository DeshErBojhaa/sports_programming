#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>
#include<vector>
#include<queue>

using namespace std;

typedef long long ll;
const ll mod=1000000007;

int node,parent;
vector<int>adj[1001];
ll used,ret,NcR[1001][1001];
bool indeg[1001];

ll dfs(int cur)
{
    ll lf=0,rh=0;
    for(int i=0; i<adj[cur].size(); i++)
    {
        rh=dfs(adj[cur][i]);
        ret*=NcR[lf+rh][lf];
        ret%=mod;

        lf+=rh;
    }
    return lf+1;
}

int main()
{
    for(int i=0;i<1001;i++) NcR[i][0]=1;

    for(int i=1;i<1001;i++)
        for(int j=1;j<=i;j++) NcR[i][j]=(NcR[i-1][j]+NcR[i-1][j-1])%mod;

    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        memset(indeg,false,sizeof indeg);

        scanf(" %d",&node);
        for(int i=1; i<=node; i++) adj[i].clear();

        for(int i=1; i<node; i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            adj[a].push_back(b);
            indeg[b]=true;
        }

        for(int i=1; i<=node; i++)
            if(!indeg[i])
            {
                parent=i;
                break;
            }

        ret=1;
        ll ans=dfs(parent);
        printf("Case %d: %lld\n",tt,ret);
    }
    return 0;
}

/*
9
1 2
1 3
2 4
2 5
4 8
4 9
3 6
3 7

*/
