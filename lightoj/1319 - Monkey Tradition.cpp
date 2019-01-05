#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

typedef long long ll;

ll prime[15],rem[15],nn,N;


void extEuclid(ll a, ll b, ll &xx, ll &yy, ll &gcd)
{
    xx = 0;
    yy = 1;
    gcd = b;
    ll m, n, q, r;
    for (ll u=1, v=0; a != 0; gcd=a, a=r)
    {
        q = gcd / a;
        r = gcd % a;
        m = xx-u*q;
        n = yy-v*q;
        xx=u;
        yy=v;
        u=m;
        v=n;
    }
}

// The result could be negative, if it's required to be positive, then add "m"
int modInv(ll number, ll mod)
{
    ll xx, yy, gcd;
    extEuclid(number, mod, xx, yy, gcd);
    if (gcd == 1) return (xx+mod)%mod;
    return 0;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        N=1;
        scanf(" %d",&nn);

        for(int i=0;i<nn;i++)
            scanf(" %lld %lld",&prime[i],&rem[i]), N*=prime[i];
ll ans=0;
        for(int i=0;i<nn;i++)
        {
            ans+=(rem[i]*(N/prime[i])*(modInv(N/prime[i],prime[i])))%N;
            ans%=N;
        }
        printf("Case %d: %lld\n",tt,ans);
    }

    return 0;
}
