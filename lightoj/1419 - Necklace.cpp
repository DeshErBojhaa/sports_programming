#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
#include<iostream>

using namespace std;

typedef long long ll;

const ll mod=1000000007;
ll ncr[1001][1001];

ll Make_pow(ll base,ll por)
{
    if(por==1) return base;
    if(por<=0) return(ll) 1;

    ll ret=Make_pow(base,por/2);
    ret=(ret*ret);
    ret%=mod;

    if(por%2) ret=(ret*base);
    ret%=mod;

    return ret;
}

int main()
{
    int T;

    for(int i=0; i<=1000; i++) for(int j=0; j<=i; j++) ncr[i][j]+=i&&j?(ncr[i-1][j-1]+ncr[i-1][j])%mod:1;

    ll N,K;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {

        scanf(" %lld %lld",&N,&K);
        ll final=0;

        ll ans=0;

        for(int out=1; out<=5; out++)
        {
            for(ll i=1; i<=N; i++)
            {
                ll up=(ll)__gcd(i,N);
                ans+=(Make_pow(out,up));
                ans%=mod;
            }
            ans+=(ans*(Make_pow(N,mod-2)));
            ans%=mod;

//            final+=(ncr[100][out]/ans);
  //          final%=mod;
        }
cout<<final<<endl;
        printf("Case %d: %lld\n",tt,ans);
    }
    return 0;
}
