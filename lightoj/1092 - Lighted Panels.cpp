#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>

using namespace std;

int T,cs,R,C;
char grid[8][8];
int dp[8][1<<8][1<<8],vis[8][1<<8][1<<8],state[8];

int move_row[]={-1,-1,-1,0,0,1,1,1};
int move_col[]={-1,0,1,-1,1,-1,0,1};

int rec(int row,int up,int mid)
{
    if(row==R)
    {
        if(up==0) return 0;
        return 10000000;
    }

    int &ret=dp[row][up][mid];
    if(vis[row][up][mid]==cs) return ret;
    ret=66;
    vis[row][up][mid]=cs;

    int use_up=up;
    int use_mid=mid;
    int use_next=state[row+1];

    for(int subset=0;subset<(1<<C);subset++)
    {
        use_up=up;
        use_mid=mid;
        use_next=state[row+1];

        for(int i=0;i<C;i++)
        {
            if(subset&(1<<i))
            {
                use_mid^=(1<<i);
                for(int j=0;j<8;j++)
                {
                    int nr=row+move_row[j];
                    int nc=i+move_col[j];

                    if(nr>=R || nr<0 || nc>=C || nc<0) continue;
                    if(nr<row) use_up^=(1<<nc);
                    if(nr==row) use_mid^=(1<<nc);
                    if(nr>row) use_next^=(1<<nc);
                }
            }
        }
        if(use_up==0) ret=min(ret,rec(row+1,use_mid,use_next)+__builtin_popcount(subset));
    }
    return ret;
}


int main()
{
    scanf(" %d",&T);
    for(cs=1; cs<T+1; cs++)
    {
        memset(state,0,sizeof state);
        scanf(" %d %d",&R,&C);
        for(int i=0; i<R; i++)
            for(int j=0; j<C; j++)
            {
                scanf(" %c",&grid[i][j]);
                if(grid[i][j]=='.') state[i]|=(1<<j);
            }
        int ans=rec(0,0,state[0]);
        if(ans>65)
            printf("Case %d: impossible\n",cs);
        else
            printf("Case %d: %d\n",cs,ans);
    }
    return 0;
}
