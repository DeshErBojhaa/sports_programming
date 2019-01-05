#include<stdio.h>
#include<iostream>
#include<sstream>
#include<string>

using namespace std;

typedef long long ll;
ll mod=1000000007,fact[1000001];
int a,b,n;

bool ck(ll sum)
{
    while(sum)
    {
        if(sum%10 != a && sum%10 !=b) return false;
        sum/=10;
    }
    return true;
}

ll bm(ll a,int b)
{
    if(b==0) return 1;
    ll ret=bm(a,b/2);
    ret=(ret*ret)%mod;
    if(b&1) ret=(ret*a)%mod;
    return ret;
}

ll find(int in)
{
    ll hor=(fact[in]*fact[n-in])%mod;

    ll inv=bm(hor,mod-2);

    return (ll)(inv*fact[n])%mod;
}

int main()
{
    cin>>a>>b>>n;
    fact[0]=1;
    for(int i=1;i<=n;i++) fact[i]=(fact[i-1]*i)%mod;

    ll sum=0;
    ll ans=0;
    int loop=(int)(n/2);

    for(int i=0;i<=(n);i++)
    {
        sum=0;
        sum+=ll(i*a)+( (n-i)*b );

        if(ck(sum)) ans+=find(i);
        ans%=mod;
    }

    cout<<ans<<endl;
    return 0;
}
