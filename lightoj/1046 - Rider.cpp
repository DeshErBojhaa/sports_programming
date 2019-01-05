#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<string.h>
#include<math.h>

using namespace std;

const int mr[]= {-1,-2,-2,-1,1,2,2,1};
const int mc[]= {2,1,-1,-2,-2,-1,1,2};

int move[11][11],num[11][11],mrow,mcol,K;
char arr[11][11];
double tmp[11][11];

bool check(int row,int col)
{
    if(row>=0 && row<mrow && col>=0 && col<mcol) return true;
    else return false;
}

void calc(int row,int col,int m)
{
    memset(tmp,0,sizeof tmp);

    queue<int>q;
    q.push(row);
    q.push(col);

    while(q.size())
    {
        int r,c,nr,nc;
        r=q.front();
        q.pop();
        c=q.front();
        q.pop();

        for(int i=0; i<8; i++)
        {
            nr=r+mr[i];
            nc=c+mc[i];

            if(check(nr,nc) && tmp[nr][nc]==0 && (nr!=row || nc!=col))
            {
                tmp[nr][nc]=tmp[r][c]+1;

                num[nr][nc]++;
                q.push(nr);
                q.push(nc);
            }
        }
    }

    for(int i=0; i<mrow; i++)
        for(int j=0; j<mcol; j++)
        {
            tmp[i][j]=ceil(tmp[i][j]/m);
            move[i][j]+=tmp[i][j];
        }
    return;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        K=0;
        memset(num,0,sizeof num);
        memset(move,0,sizeof move);

        scanf(" %d %d",&mrow,&mcol);
        for(int i=0; i<mrow; i++)
            for(int j=0; j<mcol; j++)
            {
                scanf(" %c",&arr[i][j]);
                if(arr[i][j]!='.')
                {
                    num[i][j]=1;
                    K++;
                }
            }

        for(int i=0; i<mrow; i++)
            for(int j=0; j<mcol; j++)
            {
                if(arr[i][j]!='.')
                {
                    calc(i,j,arr[i][j]-'0');
                    arr[i][j]='.';
                }
            }

        int ans=1<<30;
        for(int i=0; i<mrow; i++)
            for(int j=0; j<mcol; j++)
            {
                if(num[i][j]==K)
                    ans=min(ans,move[i][j]);
            }
        if(ans==1<<30) ans=-1;
        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}
