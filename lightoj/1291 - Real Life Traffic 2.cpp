#include<stdio.h>
#include<algorithm>
#include<vector>
#include<stack>

using namespace std;

int creation[10001],backedge[10001],n_con_sbgph[10001],sbg_no[10001],K,num,nodes,edges,ans;
bool visited[10001];
vector<int>adj[10001];
stack<int>sequence;

void dfs(int cur,int par)
{
   visited[cur]=true;
   creation[cur]=backedge[cur]=++K;
   sequence.push(cur);

    for(int i=0;i<adj[cur].size();i++)
    {
        int to=adj[cur][i];
        if(to==par) continue;
        if(visited[to]==false)
        {
            dfs(to,cur);
            backedge[cur]=min(backedge[cur],backedge[to]);
        }
        else backedge[cur]=min(backedge[cur],creation[to]);
    }
   if(backedge[cur]==creation[cur])
   {
       while(sequence.size())
       {
           int now=sequence.top();sequence.pop();
           sbg_no[now]=num;
           if(cur==now) break;
       }
       num++;
   }
   return;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf(" %d %d",&nodes,&edges);
        for(int i=0;i<nodes;i++)
        {
            adj[i].clear();
            sbg_no[i]=creation[i]=n_con_sbgph[i]=backedge[i]=0;
            visited[i]=false;
        }
        while(sequence.size()) sequence.pop();
        ans=num=K=0;

        for(int i=0;i<edges;i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            adj[a].push_back(b);
            adj[b].push_back(a);
        }

        dfs(0,-1);
//        printf("Num %d\n",num);
        for(int i=0;i<nodes;i++)
        {
            for(int j=0;j<adj[i].size();j++)
            {
                int f=i,t=adj[i][j];
                if(sbg_no[f]!=sbg_no[t])
                {
                    n_con_sbgph[sbg_no[f]]++;
                    n_con_sbgph[sbg_no[t]]++;
                }
            }
        }
//        printf("3 %d\n",n_con_sbgph[sbg_no[3]]);
        for(int i=0;i<num;i++) if(n_con_sbgph[i]==2) ans++;
        printf("Case %d: %d\n",t,(ans+1)/2);
    }
    return 0;
}


/*

5
14 18
0 1
1 2
2 3
1 3
3 4
4 5
4 6
5 6
6 7
0 8
8 9
8 10
9 10
10 11
11 12
11 13
12 13
13 14

*/
