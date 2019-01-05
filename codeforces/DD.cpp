#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include<queue>
#include<string.h>
#include<string>
#include<sstream>
#include<math.h>
#include<map>

using namespace std;

long long dp[1<<17][17],mod=1000000007;
int n;

long long rec(int mask,int cur)
{
    if(cur>n) return 0;
    if(__builtin_popcount(mask)==n) return 1;

    long long &ret=dp[mask][cur];
    if(ret!=-1) return ret;
    ret=0;

    for(int j=1; j<=n; j++)
    {
        int val=(((cur-1)+(j-1))%n)+1;

        if( ( (1<<val) & mask)==0)
        {
            ret+=(mask | (1<<val),cur+1);

        }

    }

    return ret;
}

int main()
{
    memset(dp,-1,sizeof dp);
    cin>>n;

    long long ans=0;

    for(int i=1; i<=n; i++)
    {
        ans=(ans+rec(0,1))%mod;
    }
    printf("%I64d\n",ans);
    return 0;
}
