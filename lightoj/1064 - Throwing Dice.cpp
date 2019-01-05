#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>

using namespace std;

int n_dice,limit;
unsigned long long dp[26][151];

unsigned long long rec(int cur, int sum)
{
//    printf("cur %d sum %d\n",cur,sum);
    unsigned long long ans=0;
//
//    if(cur>n_dice)
//    return 0;

    if(dp[cur][sum]!=-1)
        return dp[cur][sum];

    if(cur==n_dice)
    return sum>=limit;

    for(int i=1;i<=6;i++)
    {
        ans+=rec(cur+1,sum+i);
//        printf("ANS %llu \n",ans);
        dp[cur][sum]=ans;
    }
    return ans;
}

int main()
{
    int tt;
    scanf("%d",&tt);
    unsigned long long totalcase=1,truecase;
    for(int t=1;t<=tt;t++)
    {
        memset(dp, -1, sizeof dp);
        scanf("%d %d",&n_dice,&limit);
        totalcase=1;
        for(int i=1;i<=n_dice;i++)
        {
            totalcase*=6;
//              printf("%llu\n",totalcase);
        }
        truecase=rec(0,0);
        unsigned long long lob=truecase/__gcd(truecase,totalcase);
        unsigned long long hor=totalcase/__gcd(truecase,totalcase);
//        printf("True %llu Total %llu\n\n",truecase,totalcase);
           if(lob==hor)
           printf("Case %d: 1\n",t);
           else if(lob==0)
           printf("Case %d: 0\n",t);
           else
        printf("Case %d: %llu/%llu\n",t,lob,hor);

    }
    return 0;
}

