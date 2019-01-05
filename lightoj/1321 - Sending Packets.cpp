#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>

using namespace std;

int node,con;
double data,tme,dp[101][101];

int main()
{
    int T;
    cin>>T;

    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d %lf %lf",&node,&con,&data,&tme);

        for(int i=0;i<node;i++) for(int j=1;j<=node;j++) dp[i][j]=0.0;

        for(int i=0;i<con;i++)
        {
            int a,b;
            double val;
            scanf(" %d %d %lf",&a,&b,&val);
            dp[a][b]=val/100;
            dp[b][a]=val/100;
        }

        for(int k=0;k<node;k++)
            for(int i=0;i<node;i++)
                for(int j=0;j<node;j++)
                {
                    if(dp[i][k]>0.0000000001 && dp[k][j]>0.000000001)
                        dp[i][j]=max(dp[i][j], (dp[i][k]*dp[k][j]));
                }


        printf("Case %d: %.6lf\n",tt,(1.0/dp[0][node-1])*2.0*tme*data);
    }
    return 0;
}
