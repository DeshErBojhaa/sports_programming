#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<iostream>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

typedef long long ll;
typedef  pair<ll,ll>  pall;

ll dp[100008],coin[101],frequency[101];//range[10001];
vector< pall  > vv;

bool com(pall a, pall b)
{
    return (a.first*a.second)<(b.first*b.second);
}

int main()
{
    ll tt,n_of_coin,last_limit,man;
    scanf("%lld",&tt);
    for(int t=1; t<=tt; t++)
    {

        memset(dp, 0, sizeof dp);
        vv.clear();

        scanf("%lld %lld",&n_of_coin,&last_limit);
        for(int i=0; i<n_of_coin; i++) scanf("%lld",&coin[i]);
        for(int i=0; i<n_of_coin; i++) scanf("%lld",&frequency[i]);

        for(int i=0; i<n_of_coin; i++) vv.pb(mp(coin[i],frequency[i]));

        sort(vv.begin(),vv.end(),com);

        dp[0]=1;

        int count=0;
        long long  sum=0;
        for(int j=0; j<(int)vv.size(); j++)
        {
            sum+=vv[j].first*vv[j].second;
            for(int i=0; i<=sum && i<=last_limit ; i++)
            {
                if( (i+vv[j].first)<=sum && (i+vv[j].first)<=last_limit && dp[i] )
                    dp[i+vv[j].first]=1;
            }
        }
        for(int i=1;i<=last_limit;i++) if(dp[i]) count++;
        printf("Case %d: %d\n",t,count);

    }
    return 0;
}
