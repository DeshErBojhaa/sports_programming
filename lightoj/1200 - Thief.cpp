#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

int arr[101][3],n,w;
int dp[10001];

int rec(int weight)
{
    if(weight>w) return 0;

    int &ret=dp[weight];
    if(ret!=-1) return ret;
    ret=0;

    for(int i=0;i<n;i++)
        if(weight+arr[i][2]<=w)
        ret=max(ret,rec(weight+(arr[i][2]))+(arr[i][0]));


    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        int wife=0;
        scanf(" %d %d",&n,&w);
        for(int i=0; i<n; i++)
        {
            scanf(" %d %d %d",&arr[i][0],&arr[i][1],&arr[i][2]);
            wife+=arr[i][1]*arr[i][2];
        }
        memset(dp,-1,sizeof dp);
        w=w-wife;
        if(w<0) printf("Case %d: Impossible\n",t);
        else
        {
            int ans=rec(0);
            if(ans>=0)
                printf("Case %d: %d\n",t,ans);
            else
                printf("Case %d: 0\n",t);
        }
    }
    return 0;
}
