#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<string.h>

using namespace std;

int tot;
int R,C;
char arr[51][51];
bool flag[51][51];

bool chk(int row,int col)
{
    if((row<0 || row>=R || col<0 || col>=C) || (arr[row][col]=='.'))  return false;
    return true;
}

int dfs(int row,int col)
{
    flag[row][col]=true;
    int ans=1;
    if((flag[row+1][col]==false) && (chk(row+1,col)))
        ans+=dfs(row+1,col);
    if((flag[row][col+1]==false) && (chk(row,col+1)))
        ans+=dfs(row,col+1);
    if((flag[row-1][col]==false) && (chk(row-1,col)))
        ans+=dfs(row-1,col);
    if((flag[row][col-1]==false) && (chk(row,col-1)))
        ans+=dfs(row,col-1);

    return ans;
}

int main()
{
    scanf(" %d %d",&R,&C);
    for(int i=0; i<R; i++)
        for(int j=0; j<C; j++)
        {
            scanf(" %c",&arr[i][j]);
            if(arr[i][j]=='#')
                tot++;
        }

    if(tot<3) {printf("-1\n"); return 0;}

    for(int i=0; i<R; i++)
    {
        for(int j=0; j<C; j++)
            if(arr[i][j]=='#')
            {
                int get=dfs(i,j);
                if(get!=tot)
                {
                    printf("-1\n");
                    return 0;
                }
                break;
            }
        break;
    }

    for(int i=0; i<R; i++)
    {
        for(int j=0; j<C; j++)
        {
            if(arr[i][j]=='#')
            {
                memset(flag,false,sizeof flag);
                flag[i][j]=true;

                int get=0;

                if((flag[i+1][j]==false) && (chk(i+1,j)))
                    get+=dfs(i+1,j);
                else if((flag[i][j+1]==false) && (chk(i,j+1)))
                    get+=dfs(i,j+1);
                else if((flag[i-1][j]==false) && (chk(i-1,j)))
                    get+=dfs(i-1,j);
                else    get+=dfs(i,j-1);

                if(get<tot-1)
                {
                    printf("1\n");
                    return 0;
                }

            }
        }
    }
    printf("2\n");
    return 0;
}
