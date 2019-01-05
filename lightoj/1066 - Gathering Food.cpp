#include<stdio.h>
#include<queue>
#include<vector>
#include<string.h>
#include<string>
#include<math.h>

using namespace std;

int n,spx,spy,move[11][11];
char arr[11][11];
const int mr[]= {0,-1,0,1}, mc[]= {1,0,-1,0};

bool check(int r,int c)
{
    if(r>=0 && r<n && c>=0 && c<n) return true;
    else return false;
}

int bfs(int x,int y,int jog)
{
    queue<int>q;
    q.push(x);
    q.push(y);

    memset(move,0,sizeof move);
    while(q.size())
    {
        int row,col;
        row=q.front();
        q.pop();
        col=q.front();
        q.pop();

        char dd = 'A'+jog+1;
        arr[row][col]='.';

        for(int i=0; i<4; i++)
        {
            int nr=row+mr[i],  nc=col+mc[i];
            if(check(nr,nc) && ((arr[nr][nc]=='.') || (arr[nr][nc]==dd)) && move[nr][nc]==0)
            {
                if(arr[nr][nc]=='.')
                {
                    move[nr][nc]=move[row][col]+1;
                    q.push(nr);
                    q.push(nc);
                }
                else
                {
                    arr[nr][nc]='.';
                    spx=nr;
                    spy=nc;
                    return move[row][col]+1;
                }
            }
        }
    }

    return 1<<30;
}


int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        scanf(" %d",&n);
        int k=0;
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
            {
                scanf(" %c",&arr[i][j]);
                if(arr[i][j]=='A')
                {
                    spx=i;
                    spy=j; k++;
                }
                else if(arr[i][j]!='.' && arr[i][j]!='#') k++;

            }

        int ans=0,final=0,flag=0;
        for(int i=0; i<k-1; i++)
        {
            ans=bfs(spx,spy,i);
            if(ans==1<<30)
            {
                printf("Case %d: Impossible\n",tt);
                flag=1;
                break;
            }
            else
                final+=ans;
        }
        if(flag==0)
            printf("Case %d: %d\n",tt,final);
    }
    return 0;
}



