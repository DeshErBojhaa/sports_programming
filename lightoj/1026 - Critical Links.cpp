#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>

using namespace std;

struct data
{
    int from,to;
};
data tmp;

bool color[10009];
int n,low[10009],tm[10009],k;
vector<int>v[10009];
vector<data>ans;

bool com(data a,data b)
{
    if(a.from==b.from)
    {
        return a.to<b.to;
    }
    else
        return a.from<b.from;
}

void kaeda(void)
{
    sort(ans.begin(),ans.end(),com);
    return;
}

void dfs(int cur,int par)
{
    color[cur]=true;
    tm[cur]=low[cur]=++k;

    for(int i=0; i<v[cur].size(); i++)
    {
        int to=v[cur][i];
        if(to==par) continue;
        if(color[to]==false)
        {
            dfs(to,cur);
            low[cur]=min(low[cur],low[to]);
            if(low[to]>tm[cur])
            {
                tmp.from=min(cur,to);
                tmp.to=max(cur,to);
                ans.push_back(tmp);
            }
        }
        else
        {
            low[cur]=min(low[cur],tm[to]);
        }
    }
    return;
}

int main()
{
    int T,cur,m,in;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        ans.clear();
        k=0;
        scanf(" %d",&n);
        for(int i=0; i<n; i++)
        {
            low[i]=0;
            tm[i]=0;
            v[i].clear();
            color[i]=false;
        }
        for(int i=0; i<n; i++)
        {
            scanf(" %d (%d)",&cur,&m);
            for(int j=0; j<m; j++)
            {
                scanf(" %d",&in);
                v[cur].push_back(in);
                v[in].push_back(cur);
            }
        }
        for(int i=0; i<n; i++)
            if(color[i]==false)
                dfs(i,-1);
        kaeda();
        printf("Case %d:\n",tt);
        printf("%d critical links\n",ans.size());
        for(int i=0; i<ans.size(); i++)
            printf("%d - %d\n",ans[i].from,ans[i].to);
    }
    return 0;
}
