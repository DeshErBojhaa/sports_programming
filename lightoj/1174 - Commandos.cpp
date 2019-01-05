#include<stdio.h>
#include<vector>
#include<string.h>
#include<queue>

using namespace std;

#define pb push_back
#define mem(a,b) memset(a,b,sizeof (a))

int head[101][101],dyst[101][101];

void FW(int range)
{
    for(int k=0; k<range; k++)
        for(int i=0; i<range; i++)
            for(int j=0; j<range; j++)
                head[i][j]=min(head[i][j],(head[i][k]+head[k][j]));
    return;
}
int main()
{
    int tt,bild,Max,road,start,end,seed;
    scanf(" %d",&tt);
    for(int t=1; t<=tt; t++)
    {

        mem(head,0);
        scanf(" %d",&bild);
        for(int i=0; i<bild; i++)
        {
            for(int j=0; j<bild; j++)
                head[i][j]=0;
        }
        scanf(" %d",&road);

        for(int i=1; i<=road; i++)
        {
            scanf("%d %d",&start,&end);
            head[start][end]=1;
            head[end][start]=1;

        }
        scanf(" %d %d",&start,&end);
        FW(bild);
        for(int i=0; i<bild; i++,printf("\n"))
            for(int j=0; j<bild; j++)
            printf(" %d",head[i][j]);
        Max=-111;
        for(int i=0; i<bild; i++)
        {
            if((head[i][end])>Max)
            {
                Max=(head[end][i]);
            }
        }
        printf("Case %d: %d\n",t,Max);
    }
    return 0;
}
/*

13
16
0 1
0 2
1 3
1 4
2 4
2 5
3 6
3 7
5 8
5 9
8 10
8 11
11 1
9 11
3 4
7 10


*/
