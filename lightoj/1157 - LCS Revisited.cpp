#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<iostream>

using namespace std;

string up,dn;
int dp[1001][1001],pp[1001][1001],mod=1000007;

int rec(int ul,int dl)
{
    if(ul<0 || dl<0) return 0;

    int &ret=dp[ul][dl];
    if(ret!=-1) return ret;
    ret=0;

    if(up[ul]==dn[dl]) ret=rec(ul-1,dl-1)+1;
    else
    {
        ret=rec(ul-1,dl);
        ret=max(ret,rec(ul,dl-1));
    }
    return ret;
}

int find_sol(int ul,int dl)
{
    if(ul<0 || dl<0) return 1;
    int &ret=pp[ul][dl];
    if(ret!=-1) return ret;
    ret=0;

    if(up[ul]==dn[dl]) ret=(ret+find_sol(ul-1,dl-1))%mod;
    else
    {
        if(rec(ul-1,dl)==rec(ul,dl)) ret=(ret+find_sol(ul-1,dl))%mod;          /// check all cases
        if(rec(ul,dl-1)==rec(ul,dl)) ret=(ret+find_sol(ul,dl-1))%mod;          /// check all cases
        if(rec(ul-1,dl-1)==rec(ul,dl)) ret=(ret-find_sol(ul-1,dl-1)+mod)%mod;  /// check all cases
    }
    return ret;
}

int main()
{
    int T,lup,ldn;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        cin>>up>>dn;
        lup=up.size();
        ldn=dn.size();

        memset(dp,-1,sizeof dp);
        memset(pp,-1,sizeof pp);

        int ball=rec(lup-1,ldn-1);
        int ans=find_sol(lup-1,ldn-1)%mod;
        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
