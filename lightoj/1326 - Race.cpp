#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>

using namespace std;

int dp[1001][1001];long long ans[1001];

int rec(int n,int r)
{
    if(n==0) return !r;

    int &ret=dp[n][r];
    if(ret!=-1) return ret;
    ret=0;

    ret+=rec(n-1,r)%10056+rec(n-1,r-1)%10056;
    return ret%10056;
}

long long sol(int in)
{
    if(in==0 || in==1) return 1;

    if(ans[in]!=-1)     return ans[in];
    ans[in]=0;

    for(int i=1;i<=in;i++)
    {
        ans[in]+=(dp[in][i]*(sol(in-i)%10056))%10056;
    }

    return ans[in]%10056;
}

int main()
{
    memset(dp,-1,sizeof dp);
    memset(ans,-1,sizeof ans);

    for(int i=1;i<=1000;i++)
       for(int j=1;j<=i;j++) rec(i,j);
    long long ball=sol(1000);
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        int in;
        scanf(" %d",&in);
        printf("Case %d: %lld\n",t,sol(in)%10056);
    }
    return 0;
}
