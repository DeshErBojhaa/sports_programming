#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<iostream>

using namespace std;

int row,col,arr[9][9],sum[9],mask[270];

int rec(int mask)
{
    int cur=__builtin_popcount(mask);
    if(cur==col)
    {
        int MAX=-9;
        int MIN=999999999;

        for(int i=0;i<row;i++)
        {
            MAX=max(MAX,sum[i]);
            MIN=min(MIN,sum[i]);
        }

        return (int) MAX-MIN;
    }

    int ans=999999999;

    for(int i=0;i<col;i++)
    {
        if( (mask & (1<<i)) == 0)
        {
            int POW=1;
            for(int xx=0;xx<cur;xx++)
            {
                POW*=10;
            }

            for(int rr=0;rr<row;rr++)
                sum[rr]+=(POW*arr[rr][i]);

            ans=min(ans,rec(mask|(1<<i)));

            for(int rr=0;rr<row;rr++)
                sum[rr]-=(POW*arr[rr][i]);
        }
    }
    return ans;
}

int main()
{
    scanf(" %d %d",&row,&col);

    for(int i=0;i<row;i++)
        for(int j=0;j<col;j++)
        {
            char tmp;
            scanf(" %c",&tmp);
            arr[i][j]=tmp-'0';
        }

     int ans=(rec(0));
     printf("%d\n",ans);
    return 0;
}
