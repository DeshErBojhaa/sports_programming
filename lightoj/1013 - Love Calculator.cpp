#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

string a,b;
long long la,lb,dp[30][30],mem[30][30], sol1;

long long rec(long long aa, long long bb)
{
    long long ans=999999990;
    if(aa<0)  return bb+1;
    if(bb<0)  return aa+1;
    if(dp[aa][bb]!=-1)   return dp[aa][bb];
    if(a[aa]==b[bb])
        ans=min(ans,rec(aa-1,bb-1)+1);
    else
    {
        ans=min(ans,rec(aa-1,bb)+1);
        ans=min(ans,rec(aa,bb-1)+1);
    }
    dp[aa][bb]=ans;
    return ans;
}

long long track(int l, int ll)
{
    if(l<0 || ll<0) return 1;

    long long &ret = mem[l][ll];
    if(ret!=-1) return ret;
    ret=0;
    if(a[l]==b[ll])
        ret+=track(l-1,ll-1);
    else
    {
        if(rec(l,ll)==rec(l,ll-1)+1)
        ret+=track(l,ll-1);
        if(rec(l,ll)==rec(l-1,ll)+1)
        ret+=track(l-1,ll);
    }
    return ret;
}

int main()
{
    int tt;

    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        cin>>a;
        cin>>b;
        la=a.size();
        lb=b.size();
        memset(dp,-1, sizeof dp);
        memset(mem,-1, sizeof mem);
        sol1=rec(la-1,lb-1);
        long long ans2=track(la,lb);
        printf("Case %d: %lld %lld\n",t,sol1,ans2);
    }
    return 0;
}
