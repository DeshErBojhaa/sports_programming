#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>

using namespace std;

const int Mr[]={-1,0,1,0};
const int Mc[]={0,1,0,-1};

char maze[501][501];
bool flag[501][501];
int ans[501][501];

int bfs(int r,int c,int maxr, int maxc, int crystal)
{
    int row,col;
    queue<int>Q;
    Q.push(r);
    Q.push(c);
    while(!Q.empty())
    {
        r=Q.front();
        Q.pop();
        c=Q.front();
        Q.pop();
        for(int i=0;i<4;i++)
        {
            row=r+Mr[i];
            col=c+Mc[i];
            if(row>0 && row<=maxr && col>0 && col<=maxc && maze[row][col]!='#' && !flag[row][col])
            {
                flag[row][col]=true;
                if(maze[row][col]=='C')
                crystal++;
                Q.push(row);
                Q.push(col);
            }
        }
    }
    return crystal;
}

int main()
{
    int row,col,cass,tt,r,c,crystal,aans;
    scanf("%d",&tt);
    for(int t=1;t<=tt;t++)
    {
        scanf(" %d %d %d",&row,&col,&cass);
        for( r=1;r<=row;r++)
        for( c=1;c<=col;c++)
        scanf(" %c",&maze[r][c]);
        printf("Case %d:\n",t);
        memset(ans,-1,sizeof ans);
        for(int i=1;i<=cass;i++)
        {
            aans=0;
            scanf(" %d %d",&r,&c); /// Vajal hole ei line er variable check korte hobe
            crystal=0;
            flag[r][c]=1;
            if(maze[r][c]=='C')
            crystal++;
            if(ans[r][c]<0)
            {
                aans=bfs(r,c,row,col,crystal);
                for(int x=1;x<=row;x++)
                {
                    for(int y=1;y<=col;y++)
                    if(flag[x][y]==true && ans[x][y]<0)
                    ans[x][y]=aans;

                }
                printf("%d\n",ans[r][c]);
            }
            else
            {
                printf("%d\n",ans[r][c]);
              ;
            }
//            for( r=1;r<=row;r++,printf("\n"))
//        for( c=1;c<=col;c++)
//        printf(" %d",ans[r][c]);

        }
        memset(flag,0,sizeof flag);


    }
    return 0;
}
/*

4 5 4
..#..
.C#C.
##..#
..C#.
1 1
1 5
2 1
2 5


*/
