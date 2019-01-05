#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

const int MOD=1000000007;
long long fact[1009];
long long ncr[1002][1002],dp[1002][1002];


long long comb(int n,int r)
{
    if(n==0) return !r;
    long long &ret=ncr[n][r];
    if(ret!=-1) return ret;
    ret=0;

    ret=(comb(n-1,r)%MOD  + comb(n-1,r-1)%MOD )% MOD;
    return ret;
}

long long rec(int pos,int inv)
{
    if(inv==0) return fact[pos];

    long long &ret=dp[pos][inv];
    if(ret!=-1) return ret;
    ret=0;

    ret=( (pos-1)* (rec(pos-1,inv-1) %MOD) )%MOD;
    if(inv>1)
    ret=(ret + ( (inv-1)* (rec(pos-2,inv-2)%MOD) )%MOD )%MOD;
    return ret;
}

int main()
{
    fact[0]=1;
    for(int i=1;i<1001;i++) fact[i]=(fact[i-1]*i)%MOD;

    memset(dp,-1,sizeof dp);
    memset(ncr,-1,sizeof ncr);

    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        int n,m,k;
        scanf(" %d %d %d",&n,&m,&k);
        long long ans=0;
        ans=comb(m,k);
        ans=(ans* rec(n-k,m-k))%MOD;
        printf("Case %d: %lld\n",t,ans);
    }
    return 0;
}
