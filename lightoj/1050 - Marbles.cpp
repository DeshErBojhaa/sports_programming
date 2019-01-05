#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

double dp[501][501];

double rec(int r,int b)
{
    if(r==0 && b!=0) return 1;         /// unnecessary but takes less time
    if(b==0 && (r+b)%2==0) return 0;   /// unnecessary but takes less time
    if(r+b==1) return (b==1)?1:0;

    double &ret=dp[r][b];
    if(ret>-.5) return ret;
    ret=0.0;

    if((r+b)%2)
    {
        if(r>0)
        ret+=(r/(1.0*(r+b)))*(rec(r-1,b));
        if(b>0)
        ret+=(b/(1.0*(r+b)))*(rec(r,b-1));
    }
    else
    if(b>0)
    ret+=rec(r,b-1);
    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    memset(dp,-1,sizeof dp);
    for(int t=1;t<=T;t++)
    {
        int r,b;
        scanf(" %d %d",&r,&b);
        printf("Case %d: %.9lf\n",t,rec(r,b));
    }
    return 0;
}

