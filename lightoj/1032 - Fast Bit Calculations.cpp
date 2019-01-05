#include<stdio.h>
#include<string>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<sstream>
#include<math.h>

using namespace std;

long long n,dp[3][35][35];
string str;

string make_str(int n)
{
    string tmp;
    tmp.clear();
    int ind=0;
    while(n)
    {
        tmp+=(char)(n%2+'0');
        n=n/2;
        ind++;
    }

    reverse(tmp.begin(),tmp.end());
    return tmp;
}

long long rec(int pre,int len,int tot)
{
    if(len==0) return tot;
    long long &ret=dp[pre][len][tot];
    if(ret!=-1) return ret;
    ret=0;

    if(pre==1)
    {
        ret+=(rec(1,len-1,tot+1));
        ret+=rec(0,len-1,tot);
    }
    else
    {
        ret+=rec(1,len-1,tot);
        ret+=rec(0,len-1,tot);
    }

    return ret;
}

long long calc(string str)
{
    int len=str.size();
    if(len<=1) return 0;
    long long ans=0;
    for(int i=1; i<len; i++)
        ans+=rec(1,i-1,0);

    int last_dig=str[0]-'0',jog=0;

    for(int i=1; i<len; i++)
    {
        for(int j=0; j<str[i]-'0'; j++)
        {
                ans+=rec(j,len-i-1,jog);
        }

         if(str[i]=='1' && last_dig) jog++;

        last_dig=str[i]-'0';
    }
    return ans;
}

int main()
{
    int T;
    scanf(" %d",&T);
    memset(dp,-1,sizeof dp);
    for(int t=1; t<=T; t++)
    {
        scanf(" %lld",&n);
        str=make_str(n+1);

        long long ans=calc(str);
        printf("Case %d: %lld\n",t,ans);
    }
    return 0;
}
