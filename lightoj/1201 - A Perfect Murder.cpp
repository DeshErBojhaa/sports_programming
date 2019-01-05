#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>

using namespace std;

int n,m,a,b,dp[1009];
vector<int>v[1001];

int rec(int n)
{printf(":: %d\n",n);
    if(v[n].size()==0) return dp[n]=1;

    int &ret=dp[n];
    if(ret!=-1) return ret;
    ret=0;

    for(int i=0;i<v[n].size();i++)
    {
        ret+=rec(v[n][i]);
    }
    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf(" %d %d",&n,&m);
        for(int i=1;i<=n;i++) v[i].clear();

        for(int i=0;i<m;i++)
        {
            scanf(" %d %d",&a,&b);
            v[a].push_back(b);
            v[b].push_back(a);
        }

        memset(dp,-1,sizeof dp);
        int ans=0;
        for(int i=1;i<=n;i++) ans=max(ans,rec(i));
        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
