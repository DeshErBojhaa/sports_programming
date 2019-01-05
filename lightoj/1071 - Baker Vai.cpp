#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int dp[101][101][202],row,col,city[101][101];

int dfs(int r, int rr, int t)
{
    int ans=0;

     int c=t-r;
     int cc=t-rr;

    if(r>=row || rr>=row || c>=col || cc>=col)   return 0;

    if(dp[r][rr][t]!=-1)   return dp[r][rr][t];

    if(r==rr && c==cc )
    {
        ans=max(ans,dfs(r+1,rr,t+1) +city[r][c]);
        ans=max(ans,dfs(r,rr+1,t+1) +city[r][c]);
        ans=max(ans,dfs(r+1,rr+1,t+1) +city[r][c]);
        ans=max(ans,dfs(r,rr,t+1) +city[r][c]);
    }
    else
    {
        ans=max(ans,dfs(r+1,rr,t+1) +city[r][c] +city[rr][cc]);
        ans=max(ans,dfs(r,rr+1,t+1) +city[r][c] +city[rr][cc]);
        ans=max(ans,dfs(r+1,rr+1,t+1) +city[r][c] +city[rr][cc]);
        ans=max(ans,dfs(r,rr,t+1) +city[r][c] +city[rr][cc]);
    }
    dp[r][rr][t]=ans;
    return ans;
}


int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        scanf(" %d %d",&row, &col);
        for(int i=0; i<row; i++)
            for(int j=0; j<col; j++)
                scanf(" %d",&city[i][j]);

        int ans=0;
        memset(dp,-1,sizeof dp);
        ans=dfs(0,0,0);

        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
