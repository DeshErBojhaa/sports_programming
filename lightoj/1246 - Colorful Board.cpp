#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<math.h>

using namespace std;

typedef long long ll;
ll mod=1000000007,row,col,color;
ll ncr[202][202],dp[51][202];

ll makepow(ll base,ll topow)
{
    ll ret=1;

    while(topow)
    {
        if(topow&1) ret=(ret*base)%mod;
        base*=base;
        base%=mod;

        topow/=2;;
    }
    return ret;
}

int main()
{
    dp[0][0]=1;
    for(int i=0;i<202;i++) for(int j=0;j<=i;j++) ncr[i][j]+=i&&j?(ncr[i-1][j]+ncr[i-1][j-1])%mod:1;

    for(int i=1;i<51;i++)
        for(int j=1;j<202;j++)
            for(int k=1;k<=j;k++)
            {
                dp[i][j]+=(dp[i-1][j-k]*ncr[j][k])%mod;
                dp[i][j]%=mod;
            }

    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %lld %lld %lld",&row,&col,&color);
        ll ans=0;
        ll white=((row+1)*(col+1))/2;
        ll black=((row+1)*(col+1))-white;

        for(int i=1;i<color;i++)
        {
            ll tmp=( dp[i][white]*makepow(color-i,black) )%mod;
            tmp=(tmp * ncr[color][i])%mod;

            ans=(ans+tmp)%mod;
        }
        if(row==0 && col==0) ans=color;
        printf("Case %d: %lld\n",tt,ans);
    }
    return 0;
}
