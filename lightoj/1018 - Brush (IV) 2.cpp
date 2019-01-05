#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>

using namespace std;

struct data
{
    int x,y;
};
data tmp;
data arr[17];
int n,line[18][18],dp[1<<16];

data mv(int idx1,int idx2)
{
    int x1=arr[idx1].x;
    int y1=arr[idx1].y;
    int x2=arr[idx2].x;
    int y2=arr[idx2].y;

    tmp.x=x2-x1;
    tmp.y=y2-y1;

    return tmp;
}

int inaline(data a,data b)
{
    if((a.x*b.y)-(a.y*b.x)==0) return 0;
    else return 1;
}

int rec(int mask)
{
    if(__builtin_popcount(mask)==n) return 0;

    int &ret=dp[mask];
    if(ret!=-1) return ret;
    ret=1<<30;

    for(int i=0;i<n;i++)
    {
        if((mask & (1<<i))==0)
        {
            for(int j=1;j<n;j++)
            if((mask & (1<<j))==0)
            ret=min(ret,rec(mask| line[i][j])+1);
        }
    }
    return ret;
}


int main()
{
    int T,i,j,k;scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf(" %d",&n);
        memset(arr,0,sizeof arr);
        memset(line,0,sizeof line);
        for( i=0;i<n;i++)
        {   int a,b;
            scanf(" %d %d",&a,&b);
            tmp.x=a; tmp.y=b;
            arr[i]=tmp;
        }

        for( i=0;i<n;i++)
           for( j=i+1;j<n;j++)
           {
               for(k=0;k<n;k++)
               if(inaline(mv(i,j),mv(i,k))==0) line[i][j]|=(1<<k);  /// claculating all points which is co-linear to point i & j
                                                                    /// and storing their values doing or
           }
       memset(dp,-1,sizeof dp);

       printf("Case %d: %d\n",t,rec(0));
    }
    return 0;
}
