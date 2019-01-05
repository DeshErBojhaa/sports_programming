#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

int T,n,arr[201];
long long dp[200002];

int main()
{
     scanf(" %d",&T);
     for(int tt=1; tt<=T; tt++)
     {
          int l,h,d=99999999,tot=0,addv=0;

          scanf(" %d",&n);
          for(int i=0; i<n; i++) scanf(" %d",&arr[i]),tot+=arr[i];
          memset(dp,-1,sizeof dp);
          dp[0]=0;

          for(int xx=0; xx<n; xx++)
          {
               addv+=arr[xx];
               for(int i=addv; i>=0; i--)
               {
                    if(dp[i]!=-1)
                         dp[i+arr[xx]]=dp[i]+1;

                    if( dp[i+arr[xx]]==n/2 )
                         if(d>abs((tot-(i+arr[xx]))-(i+arr[xx])) )
                         {
                              d=abs((tot-(i+arr[xx]))-(i+arr[xx]));
                              l=min(i+arr[xx],tot-i-arr[xx]);
                              h=max(i+arr[xx],tot-i-arr[xx]);
                         }
               }

          }
          printf("Case %d: %d %d\n",tt,l,h);

     }
     return 0;
}
