#include<stdio.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<string.h>
#include<math.h>

using namespace std;

struct data
{
    int to,cost;
};
data tmp;
vector<data> v[111];
int n,pos,neg,color[111];

void dfs(int cur,int call)
{
    color[cur]=1;
    if(call==2) color[1]=0;
    for(int i=0; i<v[cur].size(); i++)
    {
        int go=v[cur][i].to, cost=v[cur][i].cost ;
        if(color[go]==0)
        {
            if(cost>0) pos+=cost;
            else neg+=abs(cost);
            dfs(go,call+1);
        }
    }

return;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        scanf(" %d",&n);
        for(int i=0; i<=n; i++) v[i].clear();
        memset(color,0,sizeof color);
        pos=0;
        neg=0;

        for(int i=0; i<n; i++)
        {
            int a,b,c;
            scanf(" %d %d %d",&a, &b, &c);
            tmp.to=b;
            tmp.cost=c;
            v[a].push_back(tmp);
            tmp.to=a;
            tmp.cost=-c;
            v[b].push_back(tmp);
        }
        dfs(1,0);
        printf("Case %d: %d\n",tt,min(pos,neg));
    }
    return 0;
}
