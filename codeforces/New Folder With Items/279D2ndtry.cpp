#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>

using namespace std;

long long arr[29],dp[1<<23][23];
int N;

long long rec(int mask,int taken)
{
//    int taken=__builtin_popcount(mask);
    if(taken==N) return 0;

    long long &ret=dp[mask][taken];
    if(ret!=-1) return ret;
    ret=(long long)(1<<30);

    for(int i=0;i<N;i++)
    {
        if((mask & (1<<i))!=0 )
        {
            for(int j=0;j<N;j++)
            {
                if( (mask & (1<<j))!=0 )
                {
                    if(arr[i]+arr[j]==arr[taken])
                    {
                        for(int k=0;k<N;k++)
                        if( (mask & (1<<k))!=0)
                        {
                            int bask=mask;
                            bask=bask^(1<<k);
                            ret=min(ret,rec(bask | (1<<taken) , taken+1));
                        }
                        ret=min(ret,rec(mask|(1<<taken) , taken+1)+1);
                    }
                }
            }
        }
    }
    return ret;
}

int main()
{
//    printf("%d\n\n",~99);
    scanf(" %d",&N);

    for(int i=0;i<N;i++)
        scanf(" %I64d",&arr[i]);

    memset(dp,-1,sizeof dp);
    long long ans=rec(1,1);
    if(ans>=(1<<30)) ans=-1;
    printf("%I64d\n",ans);
    return 0;
}
