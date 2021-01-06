#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<iostream>

using namespace std;

int h,n,dp[1009][5][33],mod=1000000009,pp[1009];
//
//int rec(int cur,int dir,int hi)
//{
//    if(cur>=n) return 1;
//
//    int &ret=dp[cur][dir][hi];
//    if(ret!=-1) return ret;
//    ret=0;
//
//    for(int i=1;i<5;i++)
//    {
//        for(int j=1;j+hi<=h;j++)
//        ret+=rec(cur+j+hi,i,hi+j);
//    }
//    return ret;
//}

int rec(int cur)
{
    printf("%d\n",cur);
    if(cur>=n) return 1;
    if(pp[cur]!=-1) return pp[cur];
    pp[cur]=0;

    for(int i=1;i<5;i++)
    {
        for(int j=1;j<=h;j++)
        pp[cur]+=rec(cur+j);
    }
    return pp[cur];
}


int main()
{
    scanf(" %d %d",&n,&h);
    memset(dp,-1,sizeof dp)    ;
    memset(pp,-1,sizeof pp);

    int ans=rec(1);
    cout<<ans<<endl;
    return 0;
}
