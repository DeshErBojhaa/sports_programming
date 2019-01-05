#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<math.h>

using namespace std;

double dp[100019];


double rec(int input)
{
    double &ret=dp[input];

    if(input==1) return 0.0;
    if(ret>-.5) return ret;
    ret=2.0;
    int cnt=0,n=sqrt(input)+1;
    for(int i=2; i<sqrt(input)+1; i++)
        if(input%i==0)
        {
            if(i!=(input/i))
            {
                cnt+=2;
                ret+=rec(i)+rec(input/i)+2;
            }
            else
            {
                cnt++;
                ret+=rec(i)+1;
            }
        }

    ret=ret/((cnt+1)*1.0);

    return ret;
}

int main()
{
    int T,in;
    scanf(" %d",&T);
    memset(dp,-1,sizeof dp);
    for(int t=1; t<=T; t++)
    {
        scanf(" %d",&in);
        printf("Case %d: %.10lf\n",t,rec(in));
    }
    return 0;
}
