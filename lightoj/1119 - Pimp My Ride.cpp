#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

int n,dp[(1<<14)+10],arr[15][15];

int rec(int mask)
{
    if(__builtin_popcount(mask)==n) return 0;

    int &ret=dp[mask];int jog=0;
    if(ret!=-1) return ret;
    ret=1<<30;

    for(int j=0; j<n; j++)
    {
        if (  ( mask&(1<<j) )==0   )
        {
            jog=arr[j][j];
            for(int i=0; i<n; i++)
            {
                if((mask & (1<<i))!=0)
                    jog+=arr[j][i];
            }
            ret=min(ret,rec( (mask | (1<<j)))+jog);
        }

    }
    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        memset(dp,-1,sizeof dp);
        scanf(" %d",&n);
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++) scanf(" %d",&arr[i][j]);
        printf("Case %d: %d\n",t,rec(0));
    }
    return 0;
}
