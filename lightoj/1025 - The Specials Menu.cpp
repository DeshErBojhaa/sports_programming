#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

string s;
long long sz,dp[61][61][2];

long long rec(int l,int r,int c)
{
    if(l>r || r<l) return c;

    long long &ret=dp[l][r][c];
    if(ret!=-1) return ret;
    ret=0;

    if(s[l]==s[r])
        ret+=rec(l+1,r-1,1);

    ret+=rec(l+1,r,c);
    ret+=rec(l,r-1,c);
    ret-=rec(l+1,r-1,c);

    return ret;
}

int main()
{
    int tc;
    scanf(" %d",&tc);
    for(int tt=1; tt<=tc; tt++)
    {
        s.clear();
        cin>>s;
        sz=s.size();

        memset(dp,-1,sizeof dp);

        long long ans=0;
        ans=rec(0,sz-1,0);

        printf("Case %d: %lld\n",tt,ans);
    }
    return 0;
}
