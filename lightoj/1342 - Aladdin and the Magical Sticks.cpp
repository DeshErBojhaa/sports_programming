#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

double dp[5500];

void calc_har()
{
    for(int i=1;i<=5000;i++)
    {
        dp[i]=dp[i-1]+(1/(1.0*i));
    }
    return ;
}

int main()
{
    calc_har();

    int T,n,a,b;double aa,bb;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        aa=0;bb=0;
        scanf(" %d",&n);
        for(int i=0;i<n;i++)
        {
            scanf(" %d %d",&a,&b);
            if(b==1) aa+=a;
            else bb+=a;
        }

        printf("Case %d: %.6lf\n",tt,(dp[n]*bb*1.0)+aa);
    }
    return 0;
}
