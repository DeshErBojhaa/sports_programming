#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>
#include<math.h>

using namespace std;

int MOD,sz,dp[(1<<10)+1][1021],frq[11];
string str;

int rec(int mask,int rem)
{
    if(__builtin_popcount(mask)==sz)
    {
        if(rem) return 0;
        else return 1;
    }

    int &ret=dp[mask][rem],va=0;
    if(ret!=-1) return ret;
    ret=0;

    for(int i=0; i<sz; i++)
    {
        if((mask & (1<<i)) == 0)
        {
            int num=(int)str[i]-'0';
            if((va & (1<<num))==0)
            {
                va=(va|(1<<num));
                ret+=rec(mask|(1<<i),(10*rem+(num))%MOD);
            }
        }
    }
    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        cin>>str;
        scanf(" %d",&MOD);
        sz=str.size();
        memset(dp,-1,sizeof dp);
        printf("Case %d: %d\n",t,rec(0,0));
    }
    return 0;
}
