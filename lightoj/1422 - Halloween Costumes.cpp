#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

int dp[101][101],arr[101];

int rec(int left,int right)
{
//    printf("L %d  R %d\n",left,right);
    if(left>=right) return 0;
    int &ret=dp[left][right];
    if(ret!=-1) return ret;
    ret=1<<30;

    ret=min(ret,rec(left+1,right)+1);

    for(int i=left+1; i<=right; i++)
    {
        if(arr[i]==arr[left])
        {
            if(left+1<=i-1) ret=min(ret, rec(left+1,i-1)+rec(i,right)+1);
            else
            {
//                printf("Calling else>> %d   %d      %d  %d\n",left+1,i-1,i,right);
                ret=min(ret,rec(i,right));
            }
        }
    }
    return ret;
}

int main()
{
    int T,ans,N;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        scanf(" %d",&N);
        for(int i=0; i<N; i++) scanf(" %d",&arr[i]);
        memset(dp,-1,sizeof dp);

        ans=rec(0,N-1)+1;
        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
