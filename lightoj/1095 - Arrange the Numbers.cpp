#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

long long NcR[1002][1002];
long long dp[1002][1002],fact[1002];

int mod=1000000007;

void fm()
{
    fact[0]=fact[1]=1;
    for(int i=2;i<=1000;i++)
    {
        fact[i]=(fact[i-1]*i)%mod;
    }

//    printf("%lld %lld %lld %lld\n\n",fact[997],fact[998],fact[999],fact[1000]);
    return ;
}

long long ncr(int N,int R)
{
    if(N==0) return !R;

    if(NcR[N][R]!=-1) return NcR[N][R];
    NcR[N][R]=0;

    NcR[N][R]=( (ncr(N-1,R)%mod)  +  (ncr(N-1,R-1)%mod) ) %mod;

    return NcR[N][R];
}

long long rec(int totpos,int invpos)
{
    if(invpos==0) return fact[totpos];
    long long &ret=dp[totpos][invpos];
    if(ret!=-1) return ret;
    ret=0;

    ret=(  (totpos-1)*(rec(totpos-1,invpos-1) %mod)  ) %mod;

    ret=(ret + ((invpos-1)*(rec(totpos-2,invpos-2) %mod) %mod )%mod)%mod;

    return ret;
}


int main()
{
    int T,n,m,k;
    fm();
    scanf(" %d",&T);

    memset(dp,-1,sizeof dp);
    memset(NcR,-1,sizeof NcR);

    for(int t=1;t<=T;t++)
    {
        long long ans=0;
        scanf(" %d %d %d",&n,&m,&k);
        ans=ncr(m,k);
        ans=(  ans * ( rec(n-k,m-k)%mod )  )%mod;
        printf("Case %d: %lld\n",t,ans);
    }
    return 0;
}
