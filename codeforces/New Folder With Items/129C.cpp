#include<stdio.h>
#include<algorithm>
#include<queue>
#include<string>
#include<string.h>
#include<vector>

using namespace std;

char fild[8][8];
bool flag[8][8][222];
vector<int>vec[8];

int mr[]= {1,0,-1,-1,-1,0,1,1,0};
int mc[]= {-1,-1,-1,0,1,1,1,0,0};

bool chk(int row,int col,int move)
{
    if(row>=8 || row<0 || col>=8 || col<0) return false;

    for(int i=0; i<vec[col].size(); i++)
    {
//        if(row==7 && col==0)
//        {
//            printf("CHK %d\n",vec[col][i]+move);
//        }
        if(vec[col][i]+move==row || vec[col][i]+move==(row+1)) return false;
    }
    return true;
}

bool dfs(int row,int col,int move)
{
    //printf("%d %d\n",row,col);
    if(move>200) return false;
    if(row==0 && col==7) return true;
    flag[row][col][move]=true;
    bool ans=false;

    for(int i=0; i<=8; i++)
    {
        int nr=row+mr[i];
        int nc=col+mc[i];

        ///  printf("OUT %d %d %d\n",nr,nc,move);
        if(flag[nr][nc][move+1]==false && chk(nr,nc,move+1) && ans==false)
        {
            ///     printf("INN %d %d %d\n",nr,nc,move);
            ans=dfs(nr,nc,move+1);
            if(ans) return ans;
        }
    }
    return ans;
}

int main()
{
    //while(1)
    {
        for(int i=0; i<8; i++)
        {
            for(int j=0; j<8; j++)
            {
                scanf(" %c",&fild[i][j]);
                if(fild[i][j]=='S') vec[j].push_back(i);
            }
        }
        memset(flag,false,sizeof flag);
        // printf("Vec[%d][%d] => %d\n",1,0,vec[1][0]);
        bool ans=dfs(7,0,0);
        if(ans) printf("WIN\n");
        else printf("LOSE\n");

    }
    return 0;
}

/*

.......A
........
........
........
........
S.......
SS......
MS......

LOSE
.......A
........
........
........
........
S.......
S.......
MS......

WIN
.......A
........
........
........
........
S.......
.S......
M.......

WIN
.......A
........
........
........
.S......
S.......
.S......
M.......

LOSE

SSSSSSSA
SSSSSSSS
SSSSSSSS
SSSSSSSS
SSSSSSSS
SSSSSSSS
SSSSSSSS
MSSSSSSS

LOSE

.......A
..SSSSSS
........
........
SSS.....
........
........
M.......

WIN

.SSSSSSA
.SSSSSSS
.SSSSSSS
.SSSSSSS
.SSSSSSS
.SSSSSSS
.SSSSSSS
MSSSSSSS

WIN

.......A
........
........
........
S.......
.SSSSSSS
S.......
M.......

LOSE

.......A
........
........
........
........
.SSSSSSS
S.......
M.......

WIN
*/
