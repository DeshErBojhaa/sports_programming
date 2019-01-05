#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
#include<iostream>
#include<stack>

using namespace std;

vector<int>v[10009];
stack<int>S;
int low[10001],tm[10001],sub_ind[10001],con_no[10001],K,cnt;
bool flag[10001];

void dfs(int cur,int par)
{
    low[cur]=tm[cur]=++K;
    flag[cur]=true;
    S.push(cur);

    for(int i=0;i<v[cur].size();i++)
    {
        int to=v[cur][i];
        if(to==par) continue;

        if(flag[to]==false)
        {
            dfs(to,cur);
            low[cur]=min(low[cur],low[to]);

        }
        else low[cur]=min(low[cur],tm[to]);
    }

    if(low[cur]==tm[cur])
    {
        while(S.size())
        {
            int cc=S.top(); S.pop();
            sub_ind[cc]=cnt;
            if(cc==cur) break;
        }
        cnt++;
    }
    return ;
}

int main()
{
    int T,n,m,ans,a,b;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf(" %d %d",&n,&m);
        for(int i=0;i<n;i++) v[i].clear();
        while(S.size()) S.pop();

        memset(low,0,sizeof low);
        memset(tm,0,sizeof tm);
        memset(sub_ind,0,sizeof sub_ind);
        memset(con_no,0,sizeof con_no);
        memset(flag,false,sizeof flag);
        ans=K=cnt=0;

        for(int i=0;i<m;i++)
        {
            scanf(" %d %d",&a,&b);
            v[a].push_back(b);
            v[b].push_back(a);
        }
        dfs(0,-1);

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<v[i].size();j++)
            {
                if(sub_ind[i]!=sub_ind[v[i][j]])
                {
                    con_no[sub_ind[i]]++;
                    con_no[sub_ind[v[i][j]]]++;
                }
            }
        }
        for(int i=0;i<cnt;i++) if(con_no[i]==2) ans++;
        printf("Case %d: %d\n",t,(ans+1)/2);
    }
    return 0;
}
