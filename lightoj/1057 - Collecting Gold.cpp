#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include<stdlib.h>
#include<math.h>

using namespace std;

struct data
{
    int r,c;
};

vector<data> V;
int row,col,dp[1<<15][16],sx,sy;
char arr[21][21];

int rec(int mask,int cur)
{
    if(__builtin_popcount(mask)==V.size()) return (max( abs(V[cur].r-sx), abs(V[cur].c-sy) ));

    int &ret=dp[mask][cur];
    if(ret!=-1) return ret;
    ret=1<<22;

    for(int i=0; i<V.size(); i++)
    {
        if(((1<<i) & mask)==0)
        {
            int cost=(max( abs(V[cur].r-V[i].r), abs(V[cur].c-V[i].c) ));
            ret=min(ret,rec(mask | (1<<i), i)+cost);
        }
    }
    return ret;
}


int main()
{
    int tc;
    scanf(" %d",&tc);
    for(int t=1; t<=tc; t++)
    {
        V.clear();
        scanf(" %d %d",&row,&col);

        for(int i=0; i<row; i++)
            for(int j=0; j<col; j++)
            {
                scanf(" %c",&arr[i][j]);
                if(arr[i][j]=='k')
                {
                    sx=i;
                    sy=j;
                }
                if(arr[i][j]=='g')
                {
                    data tmp;
                    tmp.c=j;
                    tmp.r=i;
                    V.push_back(tmp);
                }
            }
        data tmp;
        tmp.r=sx;
        tmp.c=sy;
        V.push_back(tmp);
        memset(dp,-1,sizeof dp);
        printf("Case %d: %d\n",t,rec(0,V.size()-1));
    }
    return 0;
}
