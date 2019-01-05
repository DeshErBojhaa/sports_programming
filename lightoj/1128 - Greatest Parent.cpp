#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<string>
#include<string.h>
#include<vector>

using  namespace std;

int node,query,parent[100002],value[100002],ancestor[100002][18],level[100002];
vector<int>vec[100002];

void dfs(int nn,int lev)
{
    level[nn]=lev;

    for(int i=0;i<vec[nn].size();i++)
        dfs(vec[nn][i],lev+1);
    return;
}

void pre_process()
{
    memset(ancestor,-1,sizeof ancestor);

    for(int i=0;i<node;i++)
        ancestor[i][0]=parent[i];

    for(int j=1; (1<<j) < node;j++)
        for(int i=0;i<node;i++)
            if(ancestor[i][j-1]!=-1)
                ancestor[i][j]=ancestor[  ancestor[i][j-1]  ][j-1];

     return;
}

int Query(int Node,int Lim)
{
    int ans=0,log;

    for(log=1;(1<<log)<=level[Node];log++);
    log--;

    for(int i=log;i>=0;i--)
    {
        int nod=ancestor[Node][i];
        if(value[nod]>=Lim && nod!=-1)
            Node=nod;
    }


    ans=Node;
    return ans;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        memset(ancestor,-1,sizeof ancestor);

        scanf(" %d %d",&node,&query);

        for(int i=0;i<=node;i++) vec[i].clear();
        for(int i=1;i<node;i++)
        {
            scanf(" %d %d",&parent[i],&value[i]);
            vec[parent[i]].push_back(i);
        }
        value[0]=1;

        dfs(0,1);
        pre_process();


        printf("Case %d:\n",tt);
        for(int qq=1;qq<=query;qq++)
        {
            int nd,lim;
            scanf(" %d %d",&nd,&lim);
            printf("%d\n",Query(nd,lim));
        }
    }
    return 0;
}
