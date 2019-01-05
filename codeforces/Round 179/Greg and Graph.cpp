#include <stdio.h>

int n,x,v[500],dp[500][500];
long long sum[500];
bool val[500];

int main()
{
    scanf("%d",&n);
    for(int i=0; i<n; ++i)
        for(int j=0; j<n; ++j)
            scanf("%d",&dp[i][j]);

    for(int i=0; i<n; --v[i],++i)
        scanf("%d",&v[i]);

    for(int k=n-1; k>=0; --k)
    {  printf("V[k]  %d\n",v[k]);
        val[v[k]]=1;
        for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
            {
                if(dp[i][j]>dp[i][v[k]]+dp[v[k]][j])
                    dp[i][j]=dp[i][v[k]]+dp[v[k]][j];
                if(val[i] && val[j])
                    sum[k]+=dp[i][j];
            }
    }

    printf("%lld",sum[0]);

    for(int k=1; k<n; ++k)
        printf(" %lld",sum[k]);

    return 0;
}
