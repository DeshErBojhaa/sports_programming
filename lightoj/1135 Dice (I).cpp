#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>

int dp[2][15010],mod=100000007;

int main()
{
    int T,num_dice,side,sum,cur,pre,bad;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf(" %d %d %d",&num_dice,&side,&sum);
        memset(dp,0,sizeof dp);
        dp[0][0]=1;
        for(int i=1;i<=num_dice;i++)
        {
            cur=i&1; pre=1-cur;
            dp[cur][0]=0;

            for(int j=1;j<=sum;j++)
            {
                bad=0;
                if(j-side-1>=0) bad=dp[pre][j-side-1];
                dp[cur][j]=dp[cur][j-1]+dp[pre][j-1]-bad;

                dp[cur][j]=(dp[cur][j]+mod)%mod;
            }
        }
        printf("Case %d: %d\n",t,dp[cur][sum]);
    }

    return 0;
}
