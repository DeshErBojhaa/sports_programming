#include<stdio.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include <iostream>
#include <cstring>

using namespace std;

#define pb push_back
#define mem(a,b) memset(a,b,sizeof(a))

struct pq
{
    int u, cst;
    pq(int n, int c)
    {
        u=n, cst=c;
    }
};

vector<pq> V[30001];
int Max,seed,dys[30001];
bool flag[30002];

void dfs(int bup)
{
    int dist = dys[bup];

    flag[bup]=1;

    for(int i=0; i<V[bup].size(); i++)
    {
        int val  = V[bup][i].u;
        int cost = V[bup][i].cst;

        if(!flag[val])
        {
            dys[val] = dist + cost;
            dfs(val);
        }
    }
    return;
}

int main()
{
    int tt,n_node,a,b,c,ball;
    scanf("%d",&tt);
    int tmp=0;
    for(int t=1; t<=tt; t++)
    {
        tmp=0;
        scanf(" %d",&n_node);
        for(int i=0; i<=n_node; i++)
            V[i].clear();

        for(int i=0; i<n_node-1; i++)
        {
            scanf("%d %d %d",&a, &b, &c);
            V[a].pb(pq(b,c));
            V[b].pb(pq(a,c));
        }

        dys[0] = 0;

        dfs(0);
        int _node = 0 , beshi = 0;

        for ( int i = 0 ; i <= n_node ; i++)
        {
            if ( dys[i] > beshi )
            {
                _node = i;
                beshi = dys[i];
            }
        }

        memset(flag,false,sizeof flag);
        memset(dys,0,sizeof dys);

        dfs(_node);

        beshi = 0;

        for ( int i = 0 ; i <= n_node ; i++)
        {
            if ( dys[i] > beshi )
            {
                beshi = dys[i];
            }
        }
        printf("Case %d: %d\n",t,beshi);

        memset(flag,false,sizeof flag);
        memset(dys,0,sizeof dys);

    }
    return 0;
}
