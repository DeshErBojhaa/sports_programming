#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>

using namespace std;

int mod=1000000007;
int n,arr[1001];
long long fact[1000009];

long long inv_mod(long long n,long long p)
{
    if(p==0) return 1;
    long long ret=inv_mod(n,p/2);
    ret=(ret*ret)%mod;
    if(p&1) ret=(ret*n)%mod;
    return ret;
}

long long comb(int n,int r)
{
    long long hor=(fact[r]*fact[n-r])%mod;
    hor=inv_mod(hor,mod-2);

    return (fact[n]*hor)%mod;
}

int main()
{
    fact[0]=fact[1]=1;

    for(int i=2; i<=1000008; i++) fact[i]=(fact[i-1]*i)%mod;

    int T,rem;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        rem=0;
        scanf(" %d",&n);
        for(int i=0; i<n; i++)
        {
            scanf(" %d",&arr[i]);
            rem+=arr[i];
        }

        long long ans=1;

        for(int i=n-1; i>0; i--)
        {
            ans=ans*(comb(rem-1,arr[i]-1))%mod;
            rem-=arr[i];
        }
        printf("Case %d: %lld\n",tt,ans);
    }
    return 0;
}

