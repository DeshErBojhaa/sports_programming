#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string>
#include<algorithm>
#include<sstream>
#include<iostream>

using namespace std;

typedef long long ll;

string str;
int T;
ll kom,besi,dp[24];

ll rec(int len)
{
    if(len<=0) return 0;
    if(len==2) return 10;
    if(len==1) return 10;

    ll &ret=dp[len];
    if(ret!=-1) return ret;
    ret=0;

    ret+=10*rec(len-2);

    return ret;
}


ll calc(ll inp)
{
    ll ret=0;

    stringstream ss;
    ss.clear();
    ss<<inp;
    ss>>str;
    int len=str.size();
    if(len==1) return inp+1;

    for(int i=1;i<len;i++)
        ret+=rec(i)-1;
//    for(int i=1;i<min((int)str[0]-'0',(int)str[len-1]-'0');i++)
//        ret+=rec(len-2);
//cout<<ret<<endl;
    for(int i=0;i<len/2;i++)
    {
        for(int j=1;j<=min(str[i]-'0',str[len-i-1]-'0');j++)
            ret+=rec(len-(2*(i+1)));
    }
    ll add=0;
//    cout<<ret<<endl;
//    if(len%2)
//        add=(int)str[len/2]-'0';
    return ret+add;
}

int main()
{
    memset(dp,-1,sizeof dp);
    cin>>T;
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %lld %lld",&kom,&besi);

        printf("Case %d: %lld\n",tt,calc(max(kom,besi))-calc(min(kom,besi)-1));
    }
    return 0;
}
