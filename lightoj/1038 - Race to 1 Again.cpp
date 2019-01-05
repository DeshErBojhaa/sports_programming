#include<math.h>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
#include<string>

using namespace std;

double dp[110000];

double rec(int n)
{
    printf(" %d\n",n);
    if(n==1) return 0;
    double &ret=dp[n];
    if(ret>-.5) return ret;
    ret=0.0;

    int cnt=0;

    for(int i=2;i<=n;i++)
    {
        if(n%i==0)
        {
            cnt++;
            if(i*i==n) cnt++;
            ret+=rec(n/i);
        }
    }
    return ret=n+(ret/cnt);
}

int main()
{
    int T,n;
    scanf(" %d",&T);
    memset(dp,-1,sizeof dp);
    for(int t=1;t<=T;t++)
    {
        scanf(" %d",&n);
        printf("Case %d: %lf\n",t,rec(n));
    }
    return 0;
}
