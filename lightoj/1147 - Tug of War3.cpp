#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>

using namespace std;

typedef long long ll;

int T,n,arr[101];
ll dp[100001];

int main()
{
     scanf(" %d",&T);
     for(int tt=1; tt<=T; tt++)
     {
          int tot=0,p,q,d,l,h,a,b;
          scanf(" %d",&n);
          for(int i=0; i<n; i++) scanf(" %d",&arr[i]), tot+=arr[i];
          memset(dp,0,sizeof dp);
          dp[0]=1;

          for(int j=0; j<n; j++)
               for(int i=tot-arr[j]; i>=0; i--)
                    if(dp[i]) dp[i+arr[j]]|=(dp[i]<<1);

          p=n/2;
          q=(n+1)/2;
          d=1<<28;

          for(int i=0; i<=tot; i++)
          {
                l=i; h=tot-i;
                if( (((dp[l] & ((ll)1<<p)) && (dp[h] & ((ll)1<<q))) || ((dp[h] & ((ll)1<<p)) && (dp[l] & ((ll)1<<q)))) && d>abs(l-h))
               {
                   d=abs(l-h);
                   a=l;
                   b=h;
               }
          }
          printf("Case %d: %d %d\n",tt,min(a,b),max(a,b));
     }
     return 0;
}
