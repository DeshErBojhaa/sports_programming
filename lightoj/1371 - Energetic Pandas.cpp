#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

typedef long long ll;

const int mod= 1000000007;
int T,n,bamboo[1001],panda[1001],valid[1001];

int How_Many_Less(int ind)
{
    int limit=panda[ind];

    if(limit<bamboo[ind]) return 0;
    int i;
    for( i=ind;; i++) if(i==n || bamboo[i]>limit) break;

    return i;
}

int main()
{
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        scanf(" %d",&n);

        for(int i=0; i<n; i++) scanf(" %d",&bamboo[i]);
        for(int i=0; i<n; i++) scanf(" %d",&panda[i]);

        sort(bamboo,bamboo+n);
        sort(panda,panda+n);

        for(int i=0; i<n; i++)
            valid[i]=How_Many_Less(i);

        ll ans=1;

        for(int i=0; i<n; i++)
        {
            if(valid[i]==0)
            {
                ans=0;
                break;
            }
            ans*=(valid[i]-i);
            ans%=mod;
        }

        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}
