#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
#include<iostream>

using namespace std;

int node,edge,tme,chunk_no,chunk[20009],indeg[20009],outdeg[20009];
vector<int>adj[20009],bdj[20009];
bool vis[20009];
struct data
{
    int nod,end;
};
vector<data>vec;

bool comp(data a,data b)
{
    return a.end>b.end;
}

void ordering(int cur)
{
    vis[cur]=true;
    tme++;

    for(int i=0; i<adj[cur].size(); i++)
    {
        int to=adj[cur][i];
        if(vis[to]==false)
            ordering(to);
    }
    data tmp;
    tmp.nod=cur;
    tmp.end=++tme;

    vec.push_back(tmp);

    return;
}

void scc(int cur)
{
    vis[cur]=true;
    chunk[cur]=chunk_no;
    for(int i=0;i<bdj[cur].size();i++)
    {
        int to=bdj[cur][i];

        if(vis[to]==false)
        scc(to);
    }
    return;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        memset(chunk,0,sizeof chunk);
        memset(indeg,0,sizeof indeg);
        memset(outdeg,0,sizeof outdeg);

        scanf(" %d %d",&node,&edge);
        for(int i=1; i<=node; i++)
        {
            adj[i].clear();
            bdj[i].clear();
        }
        tme=0;

        for(int i=0; i<edge; i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            adj[a].push_back(b);
            bdj[b].push_back(a);
        }

        memset(vis,false, sizeof vis);

        for(int i=1;i<=node;i++)
        if(vis[i]==false)
        {
            tme=0;
            ordering(i);
        }

        sort(vec.begin(),vec.end(),comp);
        memset(vis,false,sizeof vis);
        chunk_no=0;

        for(int i=0; i<vec.size(); i++)
        {
            if(vis[vec[i].nod]==false)
            { ///printf("CALL FROM %d\n",vec[i].nod);
                chunk_no++;
                scc(vec[i].nod);
            }
        }
///printf("NO CHUNK %d\n",chunk_no);
        for(int i=1;i<=node;i++)
        {
            for(int j=0;j<adj[i].size();j++)
            {
                int from=chunk[i];
                int to=chunk[adj[i][j]];

                if(from!=to)
                {
                    outdeg[from]++;
                    indeg[to]++;
                }
            }

        }
        int all=0,ball=0;
        for(int i=1;i<=chunk_no;i++)
        {
            if(indeg[i]==0) all++;
            if(outdeg[i]==0) ball++;
        }
        if(chunk_no==1) {all=0;ball=0;}
        printf("Case %d: %d\n",tt,max(all,ball));
    }
    return 0;
}

/*


1
10 13
1 2
1 3
2 4
4 5
2 5
3 6
7 6
7 3
8 1
5 9
9 10
10 5
5 8

*/

