#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>

using namespace std;

const int mod= 1000000009 ;
int n,h,dp[1001][31][31][31][2];

int rec(int cur,int a,int b,int c,int valid)
{
    // printf("%d %d %d %d %d\n",cur,a,b,c,valid);
    if(cur==n+1)
    {
        if(a<=h || b<=h || c<=h || !valid)
        {
            printf("%d %d %d %d %d\n",cur,a,b,c,valid);
            return 1;
        }
        return 0;
    }
    if (a==b and b==c and c==31 and valid==0) return 0;

    int &ret=dp[cur][a][b][c][valid];
    if(ret!=-1)
    {
        printf("%d %d %d %d %d\n",cur,a,b,c,valid);
        return ret;
    }
    ret=0;

    int aa=(valid?31:1), bb=a, cc=b, dd=c, na,nb,nc,nd;

    na=(aa>h?31:1);
    nb=(bb+1<=h?bb+1:31);
    nc=(cc+1<=h?cc+1:31);
    nd=(dd+1<=h?dd+1:31);
    ret=(ret+ rec(cur+1,nb,nc,nd,(na==31?0:1) ))%mod;

    na=(aa+1<=h?aa+1:31);
    nb=(bb>h?31:1);
    nc=(cc+1<=h?cc+1:31);
    nd=(dd+1<=h?dd+1:31);
    ret=(ret+ rec(cur+1,na,nc,nd, (nb==31?0:1)) )%mod;

    na=(aa+1<=h?aa+1:31);
    nb=(bb+1<=h?bb+1:31);
    nc=(cc>h?31:1);
    nd=(dd+1<=h?dd+1:31);
    ret=(ret + rec(cur+1,na,nb,nd,(nc==31?0:1)) ) %mod;

    na=(aa+1<=h?aa+1:31);
    nb=(bb+1<=h?bb+1:31);
    nc=(cc+1<=h?cc+1:31);
    nd=(dd>h?31:1);
    ret=(ret+ rec(cur+1,na,nb,nc,(nd==31?0:1)) )%mod;

    return ret;
}

int main()
{
    scanf(" %d %d",&n,&h);
    memset(dp,-1,sizeof dp);

    printf("%d\n",rec(1,1,1,1,0));
    return 0;
}


























