#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>

#include <iostream>

using namespace std;

struct data
{
    int r,c;
};

vector<data>C;
vector<int> P;
vector<int> DYS[25];

int n,last_row,last_col;
long long dp[1<<24];

int dys(data f,data s)
{
    return ((f.c-s.c)*(f.c-s.c))+((f.r-s.r)*(f.r-s.r));
}

long long rec(int mask)
{
    if(__builtin_popcount(mask)==n) return 0;

    long long &ret=dp[mask];
    if(ret!=-1) return ret;
    ret=1<<25;

    long long cost=0;
    for(int i=0; i<n; i++)
    {
        cost=0;
        if((mask&(1<<i))==0)
        {
            ret=min(ret, rec(mask|(1<<i)) + DYS[n][i] + DYS[i][n]  );
            for(int j=0; j<n; j++)
            {
                if(i==j) continue ;
                if((mask&(1<<j))==0)
                {
                    cost=DYS[n][i] + DYS[i][j]+DYS[j][n];
                    ret=min(ret,(rec( mask|(1<<i)|(1<<j) )+cost));
                }
            }
            break;
        }
    }
    return ret;
}

void path_print(int mask)
{

    if(__builtin_popcount(mask)==n) return;
    long long cost=0;
    for(int i=0; i<n; i++)
    {
        cost=0;
        if((mask&(1<<i))==0)
        {
            if( rec(mask|(1<<i)) + DYS[n][i] + DYS[i][n] ==rec(mask) )
            {
                P.push_back(i+1);
                P.push_back(0);
                path_print(mask|(1<<i));
                return ;
            }
            for(int j=0; j<n; j++)
            {
                if(i==j) continue;
                if((mask&(1<<j))==0)
                {
                    cost=DYS[n][i] + DYS[i][j]+DYS[j][n];
                    if(rec(mask)==(rec(mask|((1<<j)|(1<<i)))+cost))
                    {
                        P.push_back(i+1);
                        P.push_back(j+1);
                        P.push_back(0);
                        path_print(mask|(1<<i)|(1<<j));
                        return;
                    }
                }
            }
        }
    }

}

int main()
{
    scanf(" %d %d",&last_row,&last_col);
    scanf(" %d",&n);
    for(int i=0; i<n; i++)
    {
        int row,col;
        scanf(" %d %d",&row,&col);
        data tmp;
        tmp.r=row;
        tmp.c=col;
        C.push_back(tmp);
    }
    data tmp;
    tmp.r=last_row;
    tmp.c=last_col;
    C.push_back(tmp);

    for(int i=0; i<=n; i++)
    {
        for(int j=0; j<=n; j++)
            DYS[i].push_back(dys(C[i],C[j]));
    }

    memset(dp,-1,sizeof dp);

    long long ans=rec(0);

    cout<<ans<<endl;

    path_print(0);

    printf("0");
    for(int i=0; i<P.size(); i++)
        printf(" %d",P[i]);

    puts("");

    return 0;
}
