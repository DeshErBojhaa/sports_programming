#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>

using namespace std;

int N,M,LFT[101],RHT[101],node[202],tot_node,col_typ[202],parent[202];
vector<int>vec[202];
bool flag[202];

void make_typ_dfs(int cur,int color)
{
    col_typ[cur]=color;
    for(int i=0; i<vec[cur].size(); i++)
    {
        int to=vec[cur][i];
        if(col_typ[to]==-1)
            make_typ_dfs(to,1-color);
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
        scanf(" %d",&N);
        for(int i=0; i<N; i++)
        {
            scanf(" %d",&LFT[i]);
            node[i]=LFT[i];
        }
        scanf(" %d",&M);
        for(int i=0; i<M; i++)
        {
            scanf(" %d",&RHT[i]);
            node[N+i]=RHT[i];
        }
        tot_node=M+N;
        for(int i=0;i<=tot_node;i++) vec[i].clear();

        for(int i=0; i<M; i++)
            for(int j=0; j<N; j++)
                if((RHT[i]%LFT[j])==0)
                {
                    vec[j].push_back(N+i);
                    vec[N+i].push_back(j);
                }

        memset(col_typ,-1,sizeof col_typ);
        memset(parent,-1,sizeof parent);

        for(int i=0; i<tot_node; i++)
            if(col_typ[i]==-1) make_typ_dfs(i,0);

        int bad=0;
        for(int i=0; i<tot_node; i++)
        {
            memset(flag,false,sizeof flag);
            if(col_typ[i]) bad+=bpm(i);
        }

        printf("Case %d: %d\n",tt,bad);
    }
    return 0;
}
