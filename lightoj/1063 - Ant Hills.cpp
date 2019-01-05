#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

int n,m,low[10001],tm[10001],tt,col[10001],flag[10001];
vector<int>v[10001];

void dfs(int cur,int par)
{
    low[cur]=tm[cur]=++tt; col[cur]=1;
    int subtree=0;
    for(int i=0;i<v[cur].size();i++)
    {
        int to=v[cur][i];
        if(to==par) continue;
        if(col[to]==0)
        {
            subtree++;
            dfs(to,cur);
            low[cur]=min(low[cur],low[to]);
            if(low[to]>=tm[cur] && par!=-1) flag[cur]=1;
        }
        else
           low[cur]=min(low[cur],tm[to]);

        if(subtree>1 && par==-1) flag[cur]=1;
    }
    return;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=0;t<T;t++)
    {
        tt=0;
        scanf(" %d %d",&n,&m);
        for(int i=1;i<=n;i++) v[i].clear();

        for(int i=0;i<m;i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            v[a].push_back(b);
            v[b].push_back(a);
        }

        memset(tm,0,sizeof tm);
        memset(low,0,sizeof low);
        memset(col,0,sizeof col);
        memset(flag,0,sizeof flag);

        dfs(1,-1); int ans=0;
        for(int i=0;i<=n;i++) if(flag[i]!=0) ans++;
        printf("Case %d: %d\n",t+1,ans);
    }
    return 0;
}
