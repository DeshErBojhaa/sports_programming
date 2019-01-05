#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>

using namespace std;

#define range 47000
#define n_prime 4951

typedef long long ll;

bool flag[range];
ll prime[n_prime],T,nn,mm;

int mod=1000000007;

void sieve()
{
    int count=1;
    prime[0]=2;
    for(int i=3; i<range; i+=2)
    {
        if(!flag[i])
        {
            prime[count++]=i;
            if(i<range/i)
                for(int j=i*i; j<range; j+=(i+i))
                    flag[j]=1;
        }
    }

    return;
}

void extEuclid(ll a, ll b, ll &x, ll &y, ll &gcd)
{
    x = 0;
    y = 1;
    gcd = b;
    ll m, n, q, r;
    for (ll u=1, v=0; a != 0; gcd=a, a=r)
    {
        q = gcd / a;
        r = gcd % a;
        m = x-u*q;
        n = y-v*q;
        x=u;
        y=v;
        u=m;
        v=n;
    }
}

// The result could be negative, if it's required to be positive, then add "m"
int modInv(ll n, ll m)
{
    ll x, y, gcd;
    extEuclid(n, m, x, y, gcd);
    if (gcd == 1) return ((x % m)+m)%m;
    return 0;
}



int take_to_pow(ll base,ll topow)
{
    ll ret=1;
    while(topow>0)
    {
        if(topow%2)
            ret=(ret*base)%mod;
        topow/=2;
        base=(base*base)%mod;
    }
    return (int) ret;
}

ll sum_of_divisors(ll base,ll power)
{

    ll lob=take_to_pow(base,power+1);

    lob--;
    ll hor=modInv(base-1,mod);
    ///cout<<hor<<"   *** "<<endl;
    ll ret=(lob*hor)%mod;

    return ret;
}

ll power_factorize()
{
    ll base=sqrt((double)nn);
    ll use=nn;
    ll ans=1;

    for(int i=0; prime[i]<=base; i++)
    {
        if(use%prime[i]==0)
        {
            int pour=0;

            while(use%prime[i]==0)
            {
                use/=prime[i];
                pour++;
            }

            ans*=sum_of_divisors(prime[i],pour*mm);
            ans%=mod;
        }
    }

    if(use>1)
        ans*=sum_of_divisors(use,mm);
    ans%=mod;
    return ans;
}

int main()
{
    sieve();
    scanf(" %lld",&T);

    for(int tt=1; tt<=T; tt++)
    {
        scanf(" %lld %lld",&nn,&mm);
        ll ans = power_factorize();

        if(ans<0) ans=ans+mod;
        ans%=mod;

        printf("Case %d: %lld\n",tt,ans);

    }
    return 0;
}
