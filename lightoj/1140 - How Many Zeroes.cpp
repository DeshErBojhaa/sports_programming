#include<stdio.h>
#include<string>
#include<string.h>
#include<vector>
#include<math.h>
#include<algorithm>
#include<sstream>
#include<iostream>

using namespace std;

long long low,hi,dp[15][15];

long long rec(int len, int total)
{
    if(len==0) return total;

    long long &ret = dp[len][total];
    if(ret!=-1) return ret;
    ret = 0;

    for(int i=0;i<10;i++)
    {
        if(i==0) ret+=rec(len-1,total+1);
        else ret+=rec(len-1,total);
    }
    return ret;
}

long long calc(long long a)
{
    if(a<0) return 0;

    long long ans=0;
    string str;
    stringstream tream;

    tream<<a;
    tream>>str;

    int len=str.size();

    for(int i=1; i<len; i++)
        ans+=9*rec(i-1,0);

    if(a) for(int i=0; i<len; i++)
    {
        if(str[i]-'0'==0)
        {
            stringstream ss;
            long long add=0;
            if(i+1<len)
            {
                ss<<str.substr(i+1);
                ss>>add;
            }
            ans+=(add+1);
        }
        for(int j=( (i!=0) ? 0 : 1); j<(str[i]-'0'); j++)
        {
            int add= ( (j==0) ? 1 : 0) ;
            ans+=rec(len-1-i,add);
        }
    }
return ans+1;
}

int main()
{
    int tc;
    scanf(" %d",&tc);
    memset(dp,-1,sizeof dp);

    for(int tt=1; tt<=tc; tt++)
    {
        scanf(" %lld %lld",&low,&hi);
        long long ans=0;
        ans=calc(hi) -calc(low-1);
        printf("Case %d: %lld\n",tt,ans);
    }

    return 0;
}
