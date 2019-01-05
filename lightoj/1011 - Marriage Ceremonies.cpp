#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int arr[16][16],dp[1<<16][16];
int d;

int rec(int mask, int cur)
{


    if(__builtin_popcount(mask)==d) return 0;

    int &ret=dp[mask][cur];
    if(ret!=-1) return ret;

    for(int i=0; i<d; i++)
    {
        if((mask&(1<<i))==0 )
        {
            int ttt;
            ttt=mask|(1<<i);
            ret=max(ret,rec(ttt,cur+1)+arr[cur][i]);
        }
    }
    return ret;
}

int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        scanf("%d",&d);
        for(int i=0; i<d; i++)
            for(int j=0; j<d; j++)
                scanf("%d",&arr[i][j]);

        memset(dp,-1, sizeof dp);

        printf("Case %d: %d\n",t,rec(0,0));
    }
    memset(arr,0,sizeof(arr));
    return 0;
}
