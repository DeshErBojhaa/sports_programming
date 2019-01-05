#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;

struct data
{
    int s,e,c;
}inp[30009];

int T,n,dp[200009];

bool com(data a,data b)
{
    if(a.s<b.s) return true;
    return false;
}

int main()
{
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d",&n);
        for(int i=0;i<n;i++)
        {
            scanf(" %d %d %d",&inp[i].s,&inp[i].e,&inp[i].c);
            inp[i].s++;
            inp[i].e=inp[i].e+inp[i].s-1;
        }
        sort(inp,inp+n,com);
        memset(dp,0,sizeof dp);

        int cost=0;
        int i=0;

        for(int h=1;h<200001;h++)
        {
            while(i<n && inp[i].s==h)
            {
                dp[inp[i].e]=max(dp[inp[i].e],dp[h-1]+inp[i].c);
               // cost=max(cost,dp[inp[i].e]);
                i++;
            }
            cost=max(cost,dp[h]);
            dp[h]=max(cost,dp[h]);
        }
//        for(int i=0;i<200009;i++) cost=max(cost,dp[i]);
        printf("Case %d: %d\n",tt,cost);
    }
    return 0;
}
