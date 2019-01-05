#include<stdio.h>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

#define pu push_back
#define mem(a,b) memset(a, b, sizeof a)

bool flag[10003];
int Count,ans;

vector<int>V[10003];

void dfs(int bup,int num)
{
    if(Count==num)
    return;

    for(int i=0;i<V[bup].size();i++)
    {
        if(!flag[V[bup][i]])
        {
            flag[V[bup][i]]=true;
            Count++;
            dfs(V[bup][i],num);
        }
        else if(flag[bup])
        {
          // dfs(V[bup][i],num);
            return;
        }
    }
    return;
}

int main()
{
    int tt,N_light,ans2,con,x,y;
    vector<int>vv;
    scanf("%d",&tt);
    for(int t=1;t<=tt;t++)
    {
        scanf("%d %d",&N_light,&con);
        for(int i=0;i<=N_light+1;i++)
        {
            V[i].clear();
        }
        for(int i=1;i<=con;i++)
        {
            scanf("%d %d",&x,&y);
            V[x].pu(y);
        }
        ans=0; Count=0;
        memset(flag ,0 ,sizeof flag);
        for(int i=1;i<=10001;i++)
        {
            if(!flag[i] && V[i].size())
            {
                flag[i]=true;
                ans++;
                Count++;
                vv.pu(i);
                dfs(i,N_light);
            }
        }
         memset(flag ,0 ,sizeof flag);
         Count=0;
        for(int i=vv.size()-1;i>=0;i--)
        {
            ans2++;
            dfs(i,N_light);
        }
        printf("Case %d: %d\n",t,min(ans,ans2));

    }
    return 0;
}
