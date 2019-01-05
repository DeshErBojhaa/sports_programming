#include<stdio.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string>
#include<string.h>
#include<iostream>
#include<sstream>

using namespace std;

long long low ,hi,mod;
long long dp[11][82][82];

long long rec(int len,int sum,int m)
{
    if(len==0)
    {
        if(sum%mod==0 && m%mod==0)
            return 1;
        return 0;
    }

    long long &ret=dp[len][sum][m];
    if(ret!=-1) return ret;
    ret=0;

    for(int i=0; i<10; i++)
        {
            int x=((m*10)+i)%mod;
            ret=(ret+rec(len-1,(sum+i)%mod,x));
        }

    return ret;
}

long long calc(long long a)
{
    if(a<=0) return 0;

    string str;
    stringstream SS;

    SS<<a;
    SS>>str;

    int len=str.size();
    long long ans=0;

    for(int i=1; i<len; i++)
        for(int j=1; j<10; j++)
            ans+=rec(i-1,j%mod,j%mod);

    for(int i=1; i<str[0]-'0'; i++)
        ans += rec(len-1 , i%mod,i%mod);

    int digit=(str[0]-'0')%mod;
    int pre=digit;

    for(int i=1; i<len; i++)
    {
        for(int j=0; j<str[i]-'0'; j++)
        {
            int x=((pre*10)+j)%mod;
            ans+=rec(len-i-1,(digit+j)%mod,x);
        }
        digit=(digit+str[i]-'0')%mod;
        pre=((pre*10)+(str[i]-'0'))%mod;
    }
    return ans;
}

int main()
{
    int tc;
    scanf(" %d",&tc);

    for(int tt=1; tt<=tc; tt++)
    {
        scanf(" %lld %lld %lld",&low,&hi,&mod);
        if(mod<=83)
        {
            memset(dp,-1,sizeof dp);
            printf("Case %d: %lld\n",tt,calc(hi+1)-calc(low));
        }
        else
        printf("Case %d: 0\n",tt);
    }
    return 0;
}
