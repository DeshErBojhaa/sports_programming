#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<limits.h>

using namespace std;

int n;
int arr[101],dp[102][102][102];

int rec(int cur,int l, int r)
{
    if(cur>n) return 0;

    int &ret=dp[cur][l][r];
    if(ret!=-1) return ret;

    ret=0;
    if(arr[cur]>=arr[l] && arr[cur]<=arr[r])
    {
        ret=max(ret,rec(cur+1,l,cur)+1);
        ret=max(ret,rec(cur+1,cur,r)+1);
    }
    ret=max(ret,rec(cur+1,l,r));

    return ret;
}

int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        int ans=0;
        scanf("%d",&n);

        for(int i=1; i<=n; i++)
            scanf("%d",&arr[i]);
        arr[0]=-1;
        arr[n+1]=9999999;

        memset(dp,-1,sizeof dp);
        ans=rec(1,0,n+1);

        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
/*
5
7 7 7 7 7
5
9 8 7 6 5
5
1 2 3 4 5
5
3 9 1 5 8
8
121 710 312 611 599 400 689 611
5
3 9 1 5 8
8
121 710 312 100000 599 400 689 10000

*/
