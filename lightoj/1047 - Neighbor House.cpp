#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<limits.h>

using namespace std;

int arr[21][4],dp[21][4];
int n;

int rec(int cur, int pr)
{
    if(cur==n) return 0;

    int &ret=dp[cur][pr];
    if(ret!=-1) return ret;

    ret=INT_MAX;
    for(int i=0;i<3;i++)
    {
        if(i!=pr)
        {
            ret=min(ret,rec(cur+1,i)+arr[cur][i]);
        }
    }
    return ret;
}

int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1;t<=tt;t++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            for(int j=0;j<3;j++)
            scanf("%d",&arr[i][j]);

        memset(dp,-1,sizeof dp);

        int ans=INT_MAX;

        for(int i=0;i<3;i++)
        {

            ans=min(ans,rec(0,i));
        }
        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
