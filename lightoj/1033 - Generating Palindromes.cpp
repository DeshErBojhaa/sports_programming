#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;
string line;
int dp[101][101];
int rec(int big, int end)
{
    int ans=0;
    if(big>=end)
    return 0;
    if(dp[big][end]!=-1)
    return dp[big][end];
    if(line[big]==line[end])
    ans+=rec(big+1,end-1);

    else
    {
        ans++;
        ans+=min(rec(big+1,end),rec(big,end-1));
        dp[big][end]=ans;
    }
    return ans;
}

int main()
{
    int tt,length;
    scanf("%d",&tt);
    for(int t=1;t<=tt;t++)
    {
        memset(dp,-1,sizeof dp);
        cin>>line;
        length=line.size();
        printf("Case %d: %d\n",t,rec(0,length-1));
    }
    return 0;
}
