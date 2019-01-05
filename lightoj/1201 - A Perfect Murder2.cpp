#include<stdio.h>
#include<vector>
#include<iostream>
#include<string.h>

using namespace std;

int node,con,parent[1001],typ[1001];
vector<int>vec[1001];
bool flag[1001];

void typ_making_dfs(int cur,int color)
{
    typ[cur]=color;
    for(int i=0; i<vec[cur].size(); i++)
    {
        int to=vec[cur][i];
        if(typ[to]==-1)
            typ_making_dfs(to,!color);
    }
    return ;
}

void make_typ()
{
    for(int i=1; i<=node; i++)
    {
        if(typ[i]==-1) typ_making_dfs(i,0);
    }
    return;
}


int bpm(int cur)
{
    for(int i=0; i<vec[cur].size(); i++)
    {
        int to=vec[cur][i];
        if(flag[to]==false)
        {
            flag[to]=true;
            if(parent[to]==-1 || bpm(parent[to]))
            {
                parent[to]=cur;
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        memset(parent,-1,sizeof parent);
        memset(typ,-1,sizeof typ);

        scanf(" %d %d",&node,&con);
        for(int i=0; i<=node; i++) vec[i].clear();

        for(int i=0; i<con; i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            vec[a].push_back(b);
            vec[b].push_back(a);
        }

        make_typ();

        int bad=0;
        for(int i=1; i<=node; i++)
        {
            if(typ[i])
            {
                memset(flag,false,sizeof flag);
                bad+=bpm(i);
            }
        }
        printf("Case %d: %d\n",tt,node-bad);
    }
    return 0;
}
