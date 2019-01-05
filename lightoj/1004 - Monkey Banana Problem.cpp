#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string.h>

using namespace std;

#define pf printf

int dp[201][201],arr[201][201];


int dfs(int r,int c,int Mc)
{
    if(c>Mc || c<1)
        return 0;

    if(r>=(Mc*2)-1)
        return arr[r][1];
    if(dp[r][c]!=-1) return dp[r][c];
    dp[r][c]=0;
    if(r<Mc)
    {
        dp[r][c]=arr[r][c]+max(dfs(r+1,c,Mc),dfs(r+1,c+1,Mc));
        return dp[r][c];
    }
    else
    {
        dp[r][c]=arr[r][c]+max(dfs(r+1,c-1,Mc),dfs(r+1,c,Mc));
        return dp[r][c];
    }
}

int main()
{
    int ans,Mc,T;
    scanf("%d",&T);
    for(int w=1; w<=T; w++)
    {
        scanf("%d",&Mc);
memset(arr,-1 ,sizeof arr);
memset(dp,-1 ,sizeof dp);
        for(int i=1; i<=Mc; i++)
            for(int j=1; j<=i; j++)
                scanf("%d",&arr[i][j]);
        for(int i=Mc+1; i<=(Mc*2)-1; i++)
            for(int j=1; j<=(Mc*2)-i; j++)
                scanf("%d",&arr[i][j]);

        ans=dfs(1,1,Mc);
        pf("Case %d: %d\n",w,ans);

    }
    return 0;
}
