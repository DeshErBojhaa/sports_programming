#include<algorithm>
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<sstream>

using namespace std;

typedef long long ll;

ll dp[20][10];
ll bam,dan,first;

ll rec(int len,int now)
{
    if(len==0) return (now==first);

    ll &ret=dp[len][now];
    if(ret!=-1) return ret;
    ret=0;

    for(int i=0; i<10; i++)
        ret+=rec(len-1,i);

    return ret;
}

ll calc(ll inp)
{
    string str;
    stringstream ss;
    ss<<inp;
    ss>>str;

    int len=str.size();
    ll ans=0;

    for(int i=1; i<len; i++)
        for(int j=1; j<10; j++)
        {
            first=j;
            ans+=rec(i-1,j);
        }

    for(int i=1;i<str[0]-'0';i++)
    {
        first=i;
        ans+=rec(len-1,i);
    }

    first=str[0]-'0';

    for(int i=1;i<len;i++)
    {
        for(int j=0;j<str[i]-'0';j++)
        {
            ans+=rec(len-i-1,j);
        }

    }
    return ans;
}

int main()
{
    memset(dp,-1,sizeof dp);
    cin>>bam>>dan;

    ll ans=calc(dan+1)-calc(bam);
    cout<<ans<<endl;
}
