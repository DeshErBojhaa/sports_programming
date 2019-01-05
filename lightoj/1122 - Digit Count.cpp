#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

int m,l,arr[11],dp[11][11][2];

int rec(int p, int c, int s)
{
    if(c==l-1) return s;

    int &ret=dp[p][c][s];
    if(ret!=-1) return ret;
    ret=0;

    for(int i=0; i<m; i++)
    {
        if(s)
        {
            if(abs(p-arr[i])<=2 && abs(p-arr[i])>=0 && s)
            {
//                printf("%d %d\n",p,arr[i]);
                ret+=rec(arr[i],c+1,1);
            }
//            else
//                ret=max(ret,rec(arr[i],l-1,0));
        }
//        else
//            ret=max(ret,rec(arr[i],l-1,0));
    }
    return ret;
}

int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        scanf("%d %d",&m,&l);
        for(int i=0; i<m; i++)
            scanf("%d",&arr[i]);
        int ans=0;
        memset(dp,-1,sizeof dp);

        for(int i=0; i<m; i++)
            ans+=rec(arr[i],0,1);

        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
