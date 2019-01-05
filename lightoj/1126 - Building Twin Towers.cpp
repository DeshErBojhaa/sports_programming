#include<stdio.h>
#include<iostream>
#include<vector>
#include<string.h>
#include<algorithm>

using namespace std;

int T,arr[51],n,dp[2][250009];

int main()
{
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        int lim=0;
        scanf(" %d",&n);
        for(int i=0;i<n;i++) scanf(" %d",&arr[i]),lim+=arr[i];

        lim/=2; lim++;
        memset(dp,-1,sizeof dp);
        int now=1,pre=0,sofar=0;
        dp[pre][0]=0;

        for(int i=0;i<n;i++)
        {
            int rock=arr[i];
            for(int j=0;j<=sofar;j++)
            {
                if(j>lim) break;
                if(rock+j<=lim && dp[pre][j]!=-1) dp[now][rock+j]=max(dp[now][rock+j],dp[pre][j]);
                if(abs(rock-j)<=lim && dp[pre][j]!=-1) dp[now][abs(rock-j)]=max(dp[now][abs(rock-j)],dp[pre][j]+min(rock,j));

                dp[now][j]=max(dp[pre][j],dp[now][j]);
            }
            swap(pre,now);
            sofar+=arr[i];
        }

        printf("Case %d: ",tt);
        if(dp[pre][0]==0) printf("impossible\n");
        else printf("%d\n",dp[pre][0]);
    }
    return 0;
}

