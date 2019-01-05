#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>

using namespace std;

int n,arr[30],dp[1<<23][24];

int rec(int mask,int cur)
{
    if(cur==n) return 0;

    int &ret=dp[mask][cur];
    if(ret!=-1) return ret;
    ret=1<<30;

    int target=arr[cur];
    int sum=0;

    for(int i=0;i<=cur;i++)
    {
        if((mask & (1<<i))!=0)   /// i have in hand
        {
//            sum=arr[i];
            for(int j=0;j<=cur;j++)
            {
                if((mask & (1<<j))!=0)   /// j have in hand
                {
//                    sum+=arr[j];

                    if( (arr[i]+arr[j])==target)
                    ret=min(ret,rec(mask,cur+1));
                }
            }

        }
    }
    ret=min(ret,rec( mask|(1<<cur) , cur+1)+1);

    return ret;
}

int main()
{
    scanf(" %d",&n);
    for(int i=0;i<n;i++)
    scanf(" %d",&arr[i]);

    memset(dp,-1,sizeof dp);
    int ans=rec(0,0);
    if(ans>=1<<30) ans=0;
    printf("%d\n",ans-1);
    return 0;
}
