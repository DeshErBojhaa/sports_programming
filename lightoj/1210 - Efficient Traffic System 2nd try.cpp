#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<iostream>

using namespace std;

int n,m,chunk_no,ending[20009],outdegree[20009],indegree[20009],tme;
vector<int>front[20009],back[20009];
bool flag[20009];

struct data
{
    int node,e_time;
};
vector<data>vec;
data tmp;

bool comp(data a,data b)
{
    return a.e_time>b.e_time;
}

void forward(int cur)
{
    ++tme;
    flag[cur]=true;

    for(int i=0; i<front[cur].size(); i++)
    {
        int to=front[cur][i];

        if(flag[to]==false)
            forward(to);
    }
    tmp.node=cur;
    tmp.e_time=++tme;
    //printf("REC %d %d\n",tmp.node,tmp.e_time);
    vec.push_back(tmp);

    return;
}

void backward(int cur)
{
    flag[cur]=true;
    ending[cur]=chunk_no;
    for(int i=0; i<back[cur].size(); i++)
    {
        int to=back[cur][i];

        if(flag[to]==false)
            backward(to);
    }
    return;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        scanf(" %d %d",&n,&m);

        for(int i=1; i<=n; i++)
        {
            front[i].clear();
            back[i].clear();
        }
        memset(flag,false,sizeof flag);
        memset(ending,-1,sizeof ending);
        memset(indegree,0,sizeof indegree);
        memset(outdegree,0,sizeof outdegree);

        vec.clear();

        for(int i=0; i<m; i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            front[a].push_back(b);
            back[b].push_back(a);
        }
        tme=0;
        for(int i=1; i<=n; i++)
        {
            if(flag[i]==false)
                forward(i);
        }

        sort(vec.begin(),vec.end(),comp);
//        for(int i=0;i<vec.size();i++) printf(" ** %d",vec[i].node);
//        printf("\n");

        memset(flag,false,sizeof flag);

        chunk_no=0;
        for(int i=0; i<vec.size(); i++)
        {
            ///printf("Vec Node %d\n",vec[i].node);
            if(flag[vec[i].node]==false)
            {
                ///printf("BACK STARTING FROM %d\n",vec[i].node);
                chunk_no++;
                backward(vec[i].node);
            }
        }
        ///printf("CHUNK NO %d\n",chunk_no);
        if(chunk_no==1) printf("Case %d: 0\n",tt);
        else
        {
            for(int i=1; i<=n; i++)
                for(int j=0; j<front[i].size(); j++)
                {
                    int go_chunk,reach_chunk;
                    go_chunk=ending[i];
                    reach_chunk=ending[front[i][j]];

                    if(go_chunk!=reach_chunk)
                    {
                        outdegree[go_chunk]++;
                        indegree[reach_chunk]++;
                    }
                }

             int no_in=0,no_out=0;
             for(int i=1;i<=chunk_no;i++)
             {
                 if(outdegree[i]==0) no_out++;
                 if(indegree[i]==0) no_in++;
             }

             printf("Case %d: %d\n",tt,max(no_out,no_in));
        }
    }
    return 0;
}
