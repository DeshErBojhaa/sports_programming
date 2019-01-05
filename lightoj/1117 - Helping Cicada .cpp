#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

typedef long long ll;

ll arr[16],m,n,dp[15][16][1<<15],Nn,target;

ll rec(int lim,int last_pos,int mask)
{
    if(__builtin_popcount(mask)==lim)
    {
        ll gcd=1,lcm=1,tot=1,stt=0;

        Nn=n;

        for(int i=0; i<m; i++)
            if( (mask & (1<<i)) != 0)
            {
                gcd=(__gcd(lcm,arr[i]));
                lcm=(lcm*arr[i])/gcd;
            }

        return Nn/lcm;
    }

    ll &ret=dp[lim][last_pos][mask],start=0;
    if(ret!=-1) return ret;
    ret=0;

    for(int i=last_pos; i<m; i++)
    {
        if( (mask & (1<<i))==0 )
            ret+=rec(lim,i,mask | (1<<i));
    }
    return ret;
}

int main()
{
    ll T,ans,RES;
    cin>>T;

    for(ll tt=1; tt<=T; tt++)
    {
        scanf(" %d %d",&n,&m);

        for(int i=0; i<m; i++) scanf(" %d",&arr[i]);
        ans=n;

        for(int i=0;i<m;i++) ans-=(n/arr[i]);

        memset(dp,-1,sizeof dp);
        for(int i=2; i<=m; i++)
        {
            target=i;
            Nn=n;
            RES=rec(target,0,0);

            if(i%2) ans-=RES;
            else ans+=RES;

        }
        printf("Case %lld: %lld\n",tt,max( 0LL,ans));
    }
    return 0;
}

