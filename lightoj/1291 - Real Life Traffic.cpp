#include<stdio.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<iostream>

using namespace std;

#define rep(n) for(int i=0;i<n;i++)

int node,edge,low[10001],cnt,tm[10001],child[10001],flag[10001],K,part;
vector<int>v[10001];
stack<int>S;
bool color[10001];

void dfs(int cur,int par)
{
    color[cur]=true;
    tm[cur]=low[cur]=++K;

    S.push(cur);
    for(int i=0; i<v[cur].size(); i++)
    {
        int to=v[cur][i];
        if(to==par) continue;
        if(color[to]==false)
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
            int v=S.top();
            S.pop();
            flag[v]=part;
            if(v==cur) break;
        }
        part++;
    }
    return ;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        scanf(" %d %d",&node,&edge);
        for(int i=0; i<node; i++)
        {
            v[i].clear();
            color[i]=false;
            tm[i]=0;
            low[i]=0;
            child[i]=0;
            flag[i]=0;
        }
        while(S.size()) S.pop();
        K=cnt=part=0;

        /// clearng
        for(int i=0; i<edge; i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            v[a].push_back(b);
            v[b].push_back(a);
        }
        /// input
        dfs(0,-1);
        cout<<"*******"<<endl;
        rep(node) cout<<flag[i]<<" "; cout<<endl;
        for(int i=0; i<node; i++)
        {
            for(int j=0; j<v[i].size(); j++)
            {
                int vv=v[i][j];
///                cout<<flag[i]<<" "<<flag[vv]<<endl;
                if(flag[i]!=flag[vv])
                {
                    cout<<i<<" "<<vv<<endl;
                    child[flag[i]]++;
                    child[flag[vv]]++;
                }
            }
        }
        for(int i=0;i<part;i++) cout<<child[i]<<" ";
        for(int i=0; i<part; i++) if(child[i]==2) cnt++;
        printf("Case %d:        %d\n",t,((cnt+1)/2));
    }
    return 0;
}

/*
3

6 5
0 1
1 2
1 3
2 4
3 5

7 7
0 1
0 2
1 3
1 4
3 4
2 5
2 6

/*

17

5 4
0 1
0 2
0 3
0 4

10 10
0 1
0 2
1 2
2 3
1 4
4 5
5 6
4 7
7 8
8 9

10 11
0 1
0 2
1 2
2 3
1 4
4 5
5 6
4 7
7 8
8 7
8 9

10 13
0 1
0 4
1 2
2 3
1 3
4 5
4 6
5 6
5 7
7 8
5 8
6 9
8 9

7 9
0 1
1 2
0 2
0 3
0 4
3 4
0 5
0 6
5 6

7 6
0 1
0 2
0 3
0 4
0 5
0 6

4 3
1 2
2 3
2 0

3 3
1 2
2 0
0 1

13 17
8 0
9 6
8 6
3 10
10 11
11 3
2 4
4 5
5 2
1 6
6 7
1 7
0 1
1 2
2 3
3 0
3 12

5 4
0 1
1 2
2 3
3 4

4 4
0 1
0 2
1 2
2 3

7 6
0 1
0 2
0 3
0 4
4 5
4 6

6 5
0 1
1 2
1 3
2 4
3 5

10 9
0 1
1 2
1 3
2 4
2 5
3 6
3 7
4 8
4 9

8 10
3 1
1 7
7 4
4 6
1 5
5 0
3 2
7 6
4 1
4 3

6 7
1 0
1 3
3 4
0 2
4 5
4 1
3 0

10 10
9 8
8 1
9 5
5 4
5 0
0 3
4 6
8 7
6 2
0 8


*/
