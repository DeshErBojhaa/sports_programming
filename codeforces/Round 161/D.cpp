#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

int n,m,k;

bool flag[100009];
vector<int>vec[100009];
vector<int>ans;

bool dfs(int cur,int seq)
{
    flag[cur]=true;

    for(int i=0; i<vec[cur].size(); i++)
    {
        int to=vec[cur][i];

        if(to==1 && seq>=k) /// maybe >=
        {
            ans.push_back(cur);
            return true;
        }

        if(flag[to]==false)
        {
            bool state=dfs(to,seq+1);
            if(state) ans.push_back(cur);
            return state;
        }
    }
}

int main()
{
    scanf(" %d %d %d",&n,&m,&k);

    for(int i=0; i<m; i++)
    {
        int a,b;

        scanf(" %d %d",&a,&b);
        vec[a].push_back(b);
        vec[b].push_back(a);
    }

    ans.clear();

    for(int i=1;i<=n;i++)
    {
        if(ans.size()) break;

        memset(flag,false,sizeof flag);
        bool len=dfs(1,0);

    }

    printf("%d\n",ans.size());
    for(int i=0; i<ans.size(); i++) printf("%d ",ans[i]);
    printf("\n");

    return 0;
}
