#include<stdio.h>
#include<algorithm>

using namespace std;

int dp[1002],T,n,x,y,z;

int main()
{
     scanf(" %d",&T);
     for(int tt=1; tt<=T; tt++)
     {
          scanf(" %d %d %d %d",&n,&x,&y,&z);
          dp[0]=-x/2,dp[1]=x+y;

          for(int i=2; i<=n; i++)
          {
               dp[i]=min(dp[i-1]+z,dp[i-1]+x+y);
               for(int j=2; j<i; j++)
                    dp[i]=min(dp[i],max(dp[j-1]+z,dp[i-j]+x+y));
          }
          printf("Case %d: %d\n",tt,dp[n-1]);
     }
     return 0;
}
