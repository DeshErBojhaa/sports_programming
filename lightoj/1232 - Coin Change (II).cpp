#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

struct data
{
    int a; int b;

}arr[111];

bool com(data ii, data iii)
{
    return ii.a*ii.b<iii.a*iii.b;
}

int main()
{
    int tt,taka,last_limit,coin;
///   data arr[101];   ei khane declear korle array kaj kora na kano?
    int dp[100011];

    scanf("%d",&tt);
    for(int t=1;t<=tt;t++)
    {
        scanf("%d %d",&coin,&last_limit);
        for(int i=0;i<coin;i++)
        {
            scanf("%d",&arr[i].a);
            arr[i].b=last_limit;
        }
        sort(arr,arr+coin,com);
        int sum=0,count=0;
        memset(dp,0 ,sizeof dp);
        dp[0]=1;

        for(int i=0;i<coin;i++)
        {
            sum+=arr[i].a*arr[i].b;
            for(int j=0;j<=sum && j<=last_limit;j++)
            {
                if(j+arr[i].a<=last_limit)
                dp[j+arr[i].a]=( dp[j+arr[i].a]+dp[j])%100000007;
//                printf("index %d\n",i+arr[i].a);
            }
        }
        printf("Case %d: %d\n",t,dp[last_limit]);

    }
    return 0;
}
