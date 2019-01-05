#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

long long dp[51][51][51][2],u,n,w;

long long rec(int unit,int num,int wid,int s)
{
    if(unit==0)
    {
        if(num==0) return 1;
        else return 0;
    }

    long long &ret=dp[unit][num][wid][s];
    if(ret!=-1) return ret;
    ret=0;

    if(wid)
        ret+=rec(unit-1,num,wid,s);
    if(num)
        ret+=rec(unit-1,num-1,w,!s);

    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    memset(dp,-1,sizeof dp);
    for(int t=1; t<=T; t++)
    {
        scanf(" %d %d %d",&u,&n,&w);
//        memset(dp,-1,sizeof dp);
        printf("Case %d: %lld\n",t,rec(u-1,n-1,w-1,1));
        printf("\n-------------\n");
    }
    return 0;
}
