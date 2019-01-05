#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

int n_tower,tower[2][1001],l_r[1001],r_l[1001],dp[2][1001];

int rec(int r, int c)
{
    int ans=0;
//    int cost;
    if(c==n_tower-1)
        return tower[r][c];
    if(dp[r][c]!=-1)
        return dp[r][c];
    if(r==0)
    {
//        cost=r_l[c];
        ans=tower[r][c];
        ans+=min(rec(r,c+1),(rec(r+1,c+1)+l_r[c]));
    }
    else
    {
//        cost=l_r[c];
        ans=tower[r][c];
        ans+=min(rec(r,c+1),(rec(r-1,c+1)+r_l[c]));
    }
    dp[r][c]=ans;
    return ans;
}

int main()
{
    int T;
    scanf("%d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        memset(dp, -1, sizeof dp);
        scanf("%d",&n_tower);
        for(int i=0; i<=1; i++)
            for(int j=0; j<n_tower; j++)
                scanf("%d",&tower[i][j]);
        for(int i=0; i<n_tower-1; i++)
            scanf("%d",&l_r[i]);
        for(int i=0; i<n_tower-1; i++)
            scanf("%d",&r_l[i]);
        printf("Case %d: %d\n",tt,min(rec(0,0),rec(1,0)));
    }
    return 0;
}
