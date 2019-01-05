#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

long long dp[51][51][51],unit,pattrn,width;

long long rec(int un,int pat,int wid)
{
    if(un==0)
    {
        if(pat==0) return 1;
        else return 0;
    }
    if(pat<0 || wid<0 || un<0) return 0;

    long long &ret=dp[un][pat][wid];
    if(ret!=-1) return ret;
    ret=0;

    for(int i=1;i<=width;i++)
    {
        ret+=rec(un-i,pat-1,width);
    }
    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    memset(dp,-1,sizeof dp);
    for(int t=1;t<=T;t++)
    {
        scanf(" %d %d %d",&unit,&pattrn,&width);
        printf("Case %d: %lld\n",t,rec(unit,pattrn,width));
    }
    return 0;
}
