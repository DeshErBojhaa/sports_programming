#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<math.h>
#include<sstream>
#include<iostream>

using namespace std;

long long dp[(1<<16)+10][21];
int base,k,n;
string str;

int mv(char x)
{
    if(x>='0' && x<='9') return x-'0';
    else return x-55;
}

long long rec(int mask,int mod)
{
    int cur=__builtin_popcount(mask);
    if(cur==n )
    {
        if( mod%k==0) return 1;
        else return 0;
    }

    long long &ret=dp[mask][mod];
    if(ret!=-1) return ret;
    ret=0;

    for(int i=0; i<n; i++)
    {
        if(  (  (1<<i)& mask )==0 )
        {
            int val=mv(str[i]),pal=0;
            double mal=pow(base,(n-1-cur));
            pal=mal;

            ret+=rec(mask|(1<<i), ((mod*base)+val)%k  );  /// val*(pow(base,n-1-cur))+mod
        }
    }
    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        memset(dp,-1,sizeof dp);
        str.clear();

        scanf(" %d %d",&base,&k);
        cin>>str;
        n=str.size();

        long long ans=rec(0,0);
        printf("Case %d: %lld\n",tt,ans);
    }
}
