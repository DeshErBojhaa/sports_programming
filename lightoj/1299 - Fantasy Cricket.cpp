#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<string.h>

using namespace std;

int T,len;
long long dp[1004][1004],mod=1000000007;
bool flag[1001];
string str;

long long rec(int cur,int blank)
{
    if(cur==len) return !blank;
    long long &ret=dp[cur][blank];
    if(ret!=-1) return ret;
    ret=0;

    if(flag[cur])
    {
        ret=(ret+rec(cur+1,blank+1))%mod;
        ret=(ret+rec(cur+1,blank)*blank)%mod;
    }
    else
    {
        ret=(ret+rec(cur+1,blank-1)*blank*blank)%mod;
        ret=(ret+rec(cur+1,blank)*blank)%mod;
    }
    return ret;
}

int main()
{
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        int N=0;
        memset(flag,false,sizeof flag);
        cin>>str;
        len=str.size();
        for(int i=0; i<len; i++) if(str[i]=='U')
            {
                flag[N]=true;
                N++;
            }
            else if(str[i]=='D') N++;

        memset(dp,-1,sizeof dp);
        len=N;

        long long ans=rec(0,0);
        printf("Case %d: %lld\n",tt,ans);
    }
    return 0;
}
