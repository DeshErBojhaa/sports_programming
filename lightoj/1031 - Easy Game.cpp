#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<limits.h>

using namespace std;

int n, arr[100],dp[101][101][2];

int rec(int b, int e, int di)
{
    if(b>e || e<b) return 0;

    int &ret=dp[b][e][di];
    if(ret!=-1) return ret;

    if(!di)
    {
        for(int i=b;i<=e;i++)
        {
            ret=max(ret,rec(i,e,))
        }
    }
}

int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t =1;t<=tt;t++)
    {
        int total=0,ans;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
            total+=arr[i];
        }

        memset(dp,-1,sizeof dp);

        ans=max(rec(0,n-1,0),rec(0,n-1,1))
    }
    return 0;
}
