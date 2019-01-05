#include<stdio.h>
#include<queue>
#include<string.h>
#include<algorithm>

using namespace std;

char town[21][21];
int cost[21][21];
bool flag[21][21];
const int mrow[]={-1,0,1,0};
const int mcol[]={0,1,0,-1};

void bfs(int row, int col,int maxrow, int maxcol)
{
    int newr,newc;
    queue<int>Q;
    Q.push(row);
    Q.push(col);
    while(!Q.empty())
    {
       row= Q.front();
       Q.pop();
       col= Q.front();
       Q.pop();
       for(int i=0;i<4;i++)
       {
           newr=row+mrow[i];
           newc=col+mcol[i];
           if(newr>0 && newr<=maxrow && newc>0 && newc<=maxcol && (town[newr][newc]=='.' || town[newr][newc]=='h' || town[newr][newc]=='a' || town[newr][newc]=='b' || town[newr][newc]=='c')&& !flag[newr][newc])
           {
               cost[newr][newc]=cost[row][col]+1;
               if(town[newr][newc]=='h')
               return;
               Q.push(newr);
               Q.push(newc);
               flag[newr][newc]=true;
           }
       }
    }
}

int main()
{
    int tt,row,col,homei,homej;
    scanf("%d",&tt);
    for(int t=1;t<=tt;t++)
    {
        scanf(" %d %d",&row,&col);
        for(int i=1;i<=row;i++)
        for(int j=1;j<=col;j++)
        {
            scanf(" %c",&town[i][j]);
            if(town[i][j]=='h')
            {
                homei=i;
                homej=j;
            }
        }
        int Max=-111;
        for(int i=1;i<=row;i++)
        for(int j=1;j<=col;j++)
        {
            if(town[i][j]=='a' || town[i][j]=='b' || town[i][j]=='c')
            {
                memset(cost,0,sizeof cost);
                memset(flag,0,sizeof flag);
                flag[i][j]=true;
//                printf(" %c\n",town[i][j]);
                town[i][j]='.';
                bfs(i,j,row,col);
//                printf("Cost %d",cost[homei][homej]);
                if(cost[homei][homej]>Max)
                Max=cost[homei][homej];
            }
        }
        printf("Case %d: %d\n",t,Max);
    }
    return 0;
}
/*

10 10
##########
#..mmmma.#
#b...mm..#
#.mmmmmm.#
#.######.#
#cmmmmmm.#
#........#
#mmmmmmm.#
#........#
#h########

*/
