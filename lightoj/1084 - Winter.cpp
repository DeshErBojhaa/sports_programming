#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>

using namespace std;

int dp[100009],N,lim,pos[100009],inf=1<<30;

int rec(int cur)
{
    if(cur==N) return 0;
    if(cur>N) return inf;

    int &ret=dp[cur];
    if(ret!=-1) return ret;
    ret=inf;

    for(int i=cur+2;i<N;i++)
    {
        if(pos[i]-pos[cur]<=2*lim) ret=min(ret,rec(i+1)+1);
        else break;
    }
    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d",&N,&lim);
        for(int i=0;i<N;i++) scanf(" %d",&pos[i]);
        sort(&pos[0],&pos[N]);
//        for(int i=0;i<N;i++) printf(" %d",pos[i]); cout<<endl;
        memset(dp,-1,sizeof dp);
        int ans=rec(0);
        if(ans>=inf) ans=-1;
        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}
