#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

int n,left[1001],right[1001],l_r[1001],r_l[1001],dp[1009][1009][2];

int rec(int cur, int cost, int tower)
{
    int ans=0;
    if(tower== 1)
    {
        if(cur==(n))
            return left[n];
        if(dp[cur][cost][tower]!=-1)
            return dp[cur][cost][tower];
        ans=cost+left[cur];
        ans+=(min(rec(cur+1 , 0, 1),rec(cur+1, l_r[cur+1], 0)));
        dp[cur][cost][tower]=ans;
    }
    else
    {

        if(cur==(n))
            return right[n];
        if(dp[cur][cost][tower]!=-1)
            return dp[cur][cost][tower];
        ans=cost+right[cur];
        ans+=min(rec(cur+1, r_l[cur+1], 1),rec(cur+1,0,0));
        dp[cur][cost][tower]=ans;
    }

    return ans;
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        scanf("%d",&n);
        memset(dp,-1,sizeof dp);

        for(int i=0; i<n; i++)
            scanf("%d",&left[i]);
        for(int i=0; i<n; i++)
            scanf("%d",&right[i]);
        for(int i=1; i<n; i++)
            scanf("%d",&l_r[i]);
        l_r[0]=0;
        for(int i=1; i<n; i++)
            scanf("%d",&r_l[i]);
        r_l[0]=0;

        printf("Case %d: %d\n",tt,min(rec(0,l_r[0],1),rec(0,r_l[0],0)));
    }
    return 0;
}
