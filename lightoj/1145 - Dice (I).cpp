#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int n,si,sum,dp[1001][15001];

int rec(int cur,s)
{
    if(cur==n)
        return if(s==sum);

    int &ret=dp[cur][s];
    if(ret!=-1) return ret;

    for(int i=0;i<si;i++)
    {

    }
}

int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        scanf("%d %d %d",&n,&si,&sum);

        memset(dp,-1, sizeof dp);

        int ans=rec(0,0);
        printf("Case %d: %d\n",ans);
    }
    return 0;
}

