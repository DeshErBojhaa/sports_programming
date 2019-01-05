#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

typedef long long ll;

ll dp[100][4];

string binary_str(ll inp)
{
    string ans;
    ans.clear();

    while(inp)
    {
        if(inp%2) ans+='1';
        else ans+='0';

        inp/=2;
    }
    return ans;
}

ll rec(ll len,ll pre)
{
    if(len==0) return 1;

    ll &ret=dp[len][pre];
    if(ret!=-1) return ret;

    ret=rec(len-1,0);
    if(pre==0)
    ret+=rec(len-1,1);

    return ret;
}

ll calc(ll inp)
{
    string str=binary_str(inp);
    reverse(str.begin(),str.end());

    int len=str.size();
    ll ans=0;

    for(int i=1;i<len;i++)
        ans+=rec(i-1,1);

    ll prev=str[0]-'0';

    for(int i=1;i<len;i++)
    {
        for(int j=0;j<str[i]-'0';j++)
            ans+=rec(len-i-1,j);
        if(prev==1 && str[i]=='1')  break;
        prev=str[i]-'0';
    }
    return ans;
}






int main()
{
    int T;
    ll N,low,high,mid,val;
    string ans;

    memset(dp,-1,sizeof dp);

    scanf(" %d",&T);

    for(int t=1;t<=T;t++)
    {
        scanf(" %lld",&N);

        low=1; high=(((ll)1)<<(60));

        while(low<high)
        {
            mid=(low+high)/2;
            val=calc(mid+1);
            if(val<N)
               low=mid+1;
            else high=mid;
        }
        ans=binary_str(low);
        reverse(ans.begin(),ans.end());

        printf("Case %d: ",t);
        cout<<ans<<endl;

    }
    return 0;
}

