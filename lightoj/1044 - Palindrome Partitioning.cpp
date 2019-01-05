#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<iostream>

using namespace std;

int length,dp[1001],pali[1001][1001];
string line;

int palindrome(int b, int e)
{
    if(b>=e)
    return 1;
    if(pali[b][e]!=-1)
    return pali[b][e];
    if(line[b]!=line[e])
    return 0;
    pali[b][e]=palindrome(b+1,e-1);

    return pali[b][e];
}

int rec(int cur)
{
    if(cur==length)
    return 0;
    if(dp[cur]!=-1)
    return dp[cur];

    int ans=99999999;
    for(int i=cur;i<length;i++)
    {
        if(palindrome(cur,i))
        {
            ans=min(ans,rec(i+1)+1);
            dp[cur]=ans;
        }
    }
    return ans;
}

int main()
{
    int tt,ans;
    scanf("%d",&tt);
    for(int t=1;t<=tt;t++)
    {
        line.clear();
        cin>>line;
        memset(dp, -1, sizeof dp);
        memset(pali, -1, sizeof pali);
        length=line.size();
        printf("Case %d: %d\n",t,rec(0));
    }
    return 0;
}
