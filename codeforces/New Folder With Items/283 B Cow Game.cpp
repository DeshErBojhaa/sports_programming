#include<stdio.h>
#include<algorithm>

using namespace std;

int seq[200009],n;
long long dp[200009][2];

long long rec(int cur,int pos)
{
    if(cur<=0 || cur>n) return 0;

    long long &ret=dp[cur][pos];
    if(ret!=0) return ret;
    ret=-1;
    long long val=0;

    if(pos)
    val=rec(cur+seq[cur], 1-pos);
    else
    val=rec(cur-seq[cur], 1-pos);

    if(val==-1) return ret;

    ret=val+seq[cur];
    return ret;
}

int main()
{
    scanf(" %d",&n);
    for(int i=2;i<=n;i++) scanf(" %d",&seq[i]);

    for(int i=1;i<n;i++)
    {
        seq[1]=i;
        dp[1][1]=0;
        long long ans=rec(1,1);
        printf("%I64d\n",ans);
    }

    return 0;
}
