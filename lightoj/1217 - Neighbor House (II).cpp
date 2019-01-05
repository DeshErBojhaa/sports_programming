#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int n,arr[1001],dp[1001],limit;

int rec(int cur)
{

    if(cur>=limit) return 0;

    int &ret=dp[cur];
    if(ret!=-1) return ret;

    ret=rec(cur+2)+arr[cur];
    ret=max(ret,rec(cur+3)+arr[cur]);

    return ret;
}

int rrr(int cur)
{
    if(cur>=n) return 0;
    if(cur==n-2) return arr[0];

    int &re=dp[cur];
    if(re!=-1) return re;

    re=rrr(cur+2)+arr[cur];
    re=max(re,rrr(cur+3)+arr[cur]);

    return re;
}

int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        scanf("%d",&n);
        for(int i=0; i<n; i++)
            scanf("%d",&arr[i]);

        memset(dp,-1,sizeof dp);

        int ans=0;
        if(n>3)
        {
            limit=n-1;
            ans=rec(0);
            limit=n;
            memset(dp,-1,sizeof dp);

            ans=max(ans,rec(1));
            memset(dp,-1,sizeof dp);
            ans=max(ans,rrr(2));
        }
        else if(n==3)
            ans=max(max(arr[0],arr[1]),arr[2]);
        else
            ans=max(arr[0],arr[1]);

        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
/*

8
2
10 100
3
10 2 11
4
8 9 2 8
8
1 2 1 2 1 1 2 2
6
1 2 7 1 5 11
5
6 1 2 3 2
5
6 1 2 3 9
5
1 2 3 4 5
*/
