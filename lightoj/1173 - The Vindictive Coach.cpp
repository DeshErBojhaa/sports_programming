#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>

using namespace std;

unsigned long long dp[51][51][2];
int tot,cap;

unsigned long long rec(int low,int hi,int sign)
{
    if(low==1 && hi==0 && sign==0) return 1;

    if(hi==1 && low==0 && sign == 1) return 1;

    unsigned long long &ret=dp[low][hi][sign];
    if(ret!=-1) return ret;
    ret=0;

    if(sign)
    {
        for(int i=1;i<=hi;i++)
            ret+=rec( low+i-1, hi-i ,1-sign);
    }
    else
        for(int i=1;i<=low;i++)
          ret+=rec(i-1,low-i+hi,1-sign);

    return ret;

}

int main()
{
    int T;
    unsigned long long ans=0;

    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        scanf("%d %d",&tot,&cap);
        memset(dp,-1,sizeof dp);

        if(cap==1 && (tot == 2 || tot ==1) )ans=1;
        else if(cap==1 && tot>2)
        ans=rec(1,tot-3,0);
        else
        ans=rec(cap-1,tot-cap,0);

        printf("Case %d: ",tt); cout<<ans<<endl;
    }
    return 0;
}
