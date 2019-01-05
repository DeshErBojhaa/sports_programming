#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
#include<string>

using namespace std;

int n;
double dp[111],arr[111];

double rec(int cur)
{
    if(cur==n) return 0;

    double &ret=dp[cur];
    if(ret>-0.5) return ret;
    ret=0.0;
    int i=0;
    for( i=1; i<7; i++)
    {
        if(cur+i<n)
        ret+=arr[cur+i]+(rec(cur+i));
        else break;
    }
    if((i-1)>0) ret=ret/(i-1);
    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);

    for(int t=1; t<=T; t++)
    {
        memset(dp,-1,sizeof dp);
        scanf(" %d",&n);
        for(int i=0; i<n; i++) scanf(" %lf",&arr[i]);
        printf("Case %d: %.9lf\n",t,arr[0]+rec(0));
    }
    return 0;
}


