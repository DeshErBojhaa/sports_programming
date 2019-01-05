#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<iostream>

using namespace std;

struct data
{
    int node,end_tm;
};


int node,edge,tme;
vector<int>vec[10009];
bool vis[10009];
vector<data>arr;


bool comp(data a,data b)
{
    return a.end_tm>b.end_tm;
}

void dfs(int cur)
{
    data tmp;
    tme++;
    vis[cur]=true;
    tmp.node=cur;

    for(int i=0;i<vec[cur].size();i++)
    {
        int to=vec[cur][i];
        if(vis[to]==false)
        dfs(to);
    }
    tmp.end_tm=tme++;
    arr.push_back(tmp);
    return;
}

void ddfs(int now)
{
    vis[now]=true;
    for(int i=0;i<vec[now].size();i++)
    {
        int to=vec[now][i];
        if(vis[to]==false)
        ddfs(to);
    }
    return;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        tme=0;
        memset(vis,false,sizeof vis);
        arr.clear();

        scanf(" %d %d",&node,&edge);
        for(int i=1;i<=node;i++) vec[i].clear();

        for(int i=0;i<edge;i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            vec[a].push_back(b);
        }
        int ans=0;

        for(int i=1;i<=node;i++)
        {
            if(vis[i]==false)
            dfs(i);
        }
//        printf("LUL\n");

        sort(arr.begin(),arr.end(),comp);

        memset(vis,false,sizeof vis);

///        for(int i=0;i<arr.size();i++)
///        {
///            printf("NODE %d  END_TM %d\n",arr[i].node,arr[i].end_tm);
///        }

        for(int i=0;i<arr.size();i++)
        {
            int now=arr[i].node;
            if(vis[now]==false)
            {
                cout<<"Calling   "<<now<<endl;
                ans++;
                ddfs(now);
            }
        }

        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}

/*

6 6

1 2
2 3
3 1
4 5
5 6
6 4

6 5
1 2
3 4
5 6
2 4
4 6

*/
