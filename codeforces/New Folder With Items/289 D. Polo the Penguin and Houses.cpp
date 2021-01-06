#include<stdio.h>

using namespace std;

long long n,k,ans;
const int mod=1000000007;

int TakeToPower(int num,int rem_pow)
{
    if(rem_pow==0) return 1;

    long long ret=TakeToPower(num,rem_pow/2);
    ret=(ret*ret)%mod;
    if(rem_pow&1) ret=(ret*num)%mod;

    return (int) ret;
}

int main()
{
    scanf(" %I64d %I64d",&n,&k);

    ans=TakeToPower(k,k-1);
    ans%=mod;
    ans*=TakeToPower(n-k,n-k);
    ans%=mod;
    printf("%d\n",ans);

    return 0;
}
