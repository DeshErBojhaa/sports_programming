#include<stdio.h>
#include<algorithm>
#include<queue>
#include<string.h>
#include<string>

using namespace std;

int n,h,dp[1009][31][31][31][2];
const int mod=1000000009;

int rec(int cur,int v1,int v2,int v3,int valid)
{
    if(cur==n)
    {
        if(v1<=h || v2<=h || v3<=h || valid==0) return 1;
        return 0;
    }
    int &ret=dp[cur][v1][v2][v3][valid];
    if(ret!=-1) return ret;
    ret=0;

    int a=(valid?31:1),b=v1,c=v2,d=v3;

    int na=(a<=h?1:31),nb=(b+1<=h?b+1:31),nc=(c+1<=h?c+1:31),nd=(d+1<=h?d+1:31);
    ret=(ret+ rec(cur+1,nb,nc,nd, (na==31?1:0) ) )%mod;

    na = (a+1<=h?a+1:31);
    nb = (b>h?31:1);
    nc = (c+1<=h?c+1:31);
    nd = (d+1<=h?d+1:31);
    ret = (ret + rec(cur+1,na,nc,nd, (nb==31?1:0)) )%mod;

    na = (a+1<=h?a+1:31);
    nb = (b+1<=h?b+1:31);
    nc = (c>h?31:1);
    nd = (d+1<=h?d+1:31);
    ret = (ret + rec(cur+1,na,nb,nd, (nc==31?1:0) ) )%mod;

    na = (a+1<=h?a+1:31);
    nb = (b+1<=h?b+1:31);
    nc = (c+1<=h?c+1:31);
    nd = (d>h?31:1);
    ret = (ret+ rec(cur+1,na,nb,nc, (nd==31?1:0) ) )%mod;

    return ret;
}

int main()
{
    scanf(" %d %d",&n,&h);
    memset(dp,-1,sizeof dp);
    printf("%d\n",rec(0,1,1,1,0));
    return 0;
}
