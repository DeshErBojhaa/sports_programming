#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<math.h>

using namespace std;

int life[17];
int n,dp[1<<16];
char arr[16][16];

int rec(int mask)
{
    if(__builtin_popcount(mask)==n) return 0;

    int &ret=dp[mask];
    if(ret!=-1) return ret;
    ret=1<<29;

    for(int i=0; i<n; i++)
    {
        if((mask & (1<<i))==0)
        {
            int maxhit=1;
            for(int j=0; j<n; j++)
            {
                if((mask & (1<<j))!=0  && (arr[j][i]-'0')!=0)
                    maxhit=max(maxhit,arr[j][i]-'0');
            }
            ret=min(ret,rec((mask |(1<<i)))+(int)ceil((life[i]*1.0)/maxhit));
        }
    }
    return ret;
}

int main()
{
    int tc;
    scanf(" %d",&tc);
    for(int tt=1; tt<=tc; tt++)
    {
        scanf(" %d",&n);
        for(int i=0; i<n; i++)
            scanf(" %d",&life[i]);

        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                scanf(" %c",&arr[i][j]);

        memset(dp,-1, sizeof dp);
        int ans=0;
        ans=rec(0);
        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}
