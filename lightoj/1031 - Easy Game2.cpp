#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

int dp[101][101],arr[101];
bool vis[101][101];

int rec(int l,int r)
{
    if(l>r) return 0;
    if(l==r) return arr[l];

    int &ret=dp[l][r];
    if(vis[l][r]) return ret;
    ret=-99999999;
    vis[l][r]=true;
    int val=0;

    for(int i=l;i<=r;i++)
    {
        val+=arr[i];
        ret=max(ret,val-rec(i+1,r));
    }
    val=0;
    for(int i=r;i>=l;i--)
    {
        val+=arr[i];
        ret=max(ret,val-rec(l,i-1));
    }

    return ret;
}

int main()
{
    int T,n;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        memset(vis,false,sizeof vis);
//        memset(dp,0,sizeof dp);
        scanf(" %d",&n);
        for(int i=0; i<n; i++) scanf(" %d",&arr[i]);
        printf("Case %d: %d\n",t,rec(0,n-1));
    }
    return 0;
}
