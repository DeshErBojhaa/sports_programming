#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<string>
#include<sstream>
#include<ctype.h>
#include<vector>
#include<map>
#include<queue>
#include<math.h>
#include<algorithm>
#include<set>

#define pb push_back
#define PI acos(-1.0)
#define SZ(a) (int)a.size()
#define csprnt printf("Case %d: ", cas++);
#define EPS 1e-9
#define MAX 1000010LL*10010LL
#define MM 110000
#define ll long long
#define INF (1<<30)
#define pii pair<int, int>
#define MP make_pair
#define mod 100000007

using namespace std;

set<ll>arr;
vector<ll>num;
ll dp[MM];

void init()
{
	ll i, j, now;
	ll lim = sqrt(MAX);
	for(i=2;i<=lim;i++)
	{
		now=i*i;
		while(now<=MAX)
		{
			arr.insert(now);
			now*=i;
		}
	}
	return;
}

ll rec(int now)
{
	ll &ret = dp[now];
	if(ret!=-1) return ret;
	if(now<=1) return ret=1;
	ret=0;
	int i;
	for(i=0;i<now;i++)
		ret=(ret + (rec(i)%mod)*(rec(now-i-1)%mod))%mod;
	return ret;
}

int main()
{
	init();
	set<ll>::iterator it;
	vector<ll>::iterator low, upp;

	for(it=arr.begin();it!=arr.end();it++)
		num.pb(*it);

	memset(dp, -1, sizeof dp);
    int t, cas=1;
    scanf("%d", &t);
    while(t--)
    {
		ll a, b, n;
		ll ans;
		scanf("%lld%lld", &a, &b);
		upp = upper_bound(num.begin(), num.end(), b); low = upper_bound(num.begin(), num.end(), a-1);
		n = int(upp-low);
		ans=0;
		if(n) ans = rec(n);
		csprnt;
		printf("%lld\n", ans);
    }
    return 0;
}

