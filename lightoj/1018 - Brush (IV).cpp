#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<iostream>

using namespace std;

int dp[1<<16],xx[17],yy[17],n,line[17][17];

struct data
{
    int x, y;
};
data tmp;
data mv(int ind1,int ind2)
{
    int x1,x2,y1,y2;
    x1=xx[ind1]; y1=yy[ind1];
    x2=xx[ind2]; y2=yy[ind2];

    tmp.x=x2-x1;
    tmp.y=y2-y1;
    return tmp;
}

int cross(data a,data b)
{
    return (a.x*b.y)-(a.y*b.x);
}

int rec(int mask)
{
    ///cout<<"LUL"<<endl;
    if(__builtin_popcount(mask)==n) {cout<<"RET "<<endl;return 0;}

    int &ret=dp[mask];
    if(ret!=-1) return ret;
    ret=111;

    for(int i=0; i<n; i++)
    {
        if((mask & (1<<i))==0)
        {
            for(int j=i+1;j<n;j++)
            {
                if((mask & (1<<j))==0)
                ret=min(ret,rec(mask | line[i][j])+1);
            }
            break;
        }
    }
    return ret;
}

int main()
{
    int T,mask,i,j,k;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        scanf(" %d",&n);
        for( i=0; i<n; i++)
            scanf(" %d %d",&xx[i],&yy[i]);
        memset(dp,-1,sizeof dp);
//        cout<<"64"<<endl;
        for( i=0; i<n; i++)
        {
            for( j=i+1; j<n; j++)
            {
                mask=0;
//                mask=(1<<i)| (1<<j);
                for( k=0; k<n; k++)
                    if(cross(mv(i,j),mv(i,k))==0)
                        mask|=(1<<k);
            }
            line[i][j]=mask;
        }
//cout<<"MAIN"<<endl;
        printf("Case %d: %d\n",t,rec(0));
    }
    return 0;
}
