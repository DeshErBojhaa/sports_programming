#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<vector>
#include <iostream>

using namespace std;

struct data
{
    int r,c;
};

int I,II,III,rr,cc,dp[1<<14][24][3];
vector<data> V;
vector<int>path;

int rec(int mask,int ii,int iii)
{
    if(__builtin_popcount(mask)==III) return (((V[ii].r-I)*(V[ii].r-I))+((V[ii].c-II)*(V[ii].c-II)));

    int &ret=dp[mask][ii][iii];
    if(ret!=-1) return ret;
    ret=1<<24;

    if(iii==2)
        ret=min(ret,rec(mask,III,0)+(((V[ii].r-I)*(V[ii].r-I))+((V[ii].c-II)*(V[ii].c-II))));
    else
        for(int i=0; i<III; i++)
            if((mask&(1<<i))==0)
                if(iii<=1)
                    ret=min(ret,rec(mask|(1<<i),i,iii+1)+(((V[ii].r-V[i].r)*(V[ii].r-V[i].r))+((V[ii].c-V[i].c)*(V[ii].c-V[i].c))));

    return ret;
}

int main()
{
    scanf(" %d %d",&I,&II);
    scanf(" %d",&III);

    for(int i=0; i<III; i++)
    {
        scanf(" %d %d",&rr,&cc);
        data tmp;
        tmp.r=rr;
        tmp.c=cc;
        V.push_back(tmp);
    }
    data tmp;
    tmp.r=I;
    tmp.c=II;
    V.push_back(tmp);

    memset(dp,-1,sizeof dp);
    int ans=rec(0,III,0);
    printf("%d\n",ans);
    return 0;
}
