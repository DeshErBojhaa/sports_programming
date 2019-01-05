#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<string.h>
#include<algorithm>

using namespace std;

typedef long long ll;
ll MAXL=10000000002;ll SQRL=100022,a,b,dp[1000004];
int mod=100000007;
set<ll>st;
vector<ll>vec;

void pre()
{
    st.clear();

    for(ll i=2;i<=SQRL;i++)
    {
        ll ans=i*i;
        if(ans<=MAXL)
        {
            while(ans<=MAXL)
            {
                st.insert(ans);
                ans*=i;
            }
        }
    }
    return;
}

ll rec(ll rem)
{
    if(rem==0) return 1;

    ll &ret=dp[rem];
    if(ret!=-1) return ret;
    ret=0;

    for(int i=0;i<rem;i++)
    {
        ret=ret+(rec(i)%mod*rec(rem-i-1)%mod);
        ret%=mod;
    }
    return ret;
}

int main()
{
    memset(dp,-1,sizeof dp);
    pre();
    set<ll>::iterator it;
    vector<ll>::iterator low, hi;

    for(it=st.begin();it!=st.end();it++)
        vec.push_back(*it);

    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %lld %lld",&a,&b);

        low=upper_bound(vec.begin(),vec.end(), a-1);
        hi=upper_bound(vec.begin(),vec.end(),b);

        ll range=hi-low;

        if(range) printf("Case %d: %lld\n",tt,rec(range));
        else printf("Case %d: 0\n",tt);
    }
    return 0;
}
