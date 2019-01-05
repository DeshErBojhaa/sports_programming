#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<vector>

using namespace std;

int T,maaa,wooo;
int parent[51];
bool flag[51];
struct data
{
    int hight,age,biya;
};
data tmp;
vector<data>man,woman;
vector<int>adj[51];

int bpm(int cur)
{
    if(flag[cur]) return 0;
    flag[cur]=true;
    for(int i=0;i<adj[cur].size();i++)
    {
        int to=adj[cur][i];
        if(parent[to]==-1 || bpm(parent[to]))
        {
            parent[to]=cur; return 1;
        }
    }
    return 0;
}

int max_match()
{
    int ans=0;
    for(int i=0;i<maaa;i++)
    {
        memset(flag,false,sizeof flag);
        ans+=bpm(i);
    }
    return ans;
}

int main()
{
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d",&maaa,&wooo);
        man.clear();
        woman.clear();

        for(int i=0;i<maaa;i++)
        {
            int high,age,biya;
            scanf(" %d %d %d",&high,&age,&biya);
            tmp.hight=high;
            tmp.biya=biya;
            tmp.age=age;

            man.push_back(tmp);
            adj[i].clear();

        }

        for(int i=0;i<wooo;i++)
        {
            int high,age,biya;
            scanf(" %d %d %d",&high,&age,&biya);
            tmp.hight=high;
            tmp.biya=biya;
            tmp.age=age;

            woman.push_back(tmp);
        }

        for(int i=0;i<maaa;i++)
            for(int j=0;j<wooo;j++)
                if( abs(man[i].age-woman[j].age)<6 && abs(man[i].hight-woman[j].hight)<13 && (man[i].biya==woman[j].biya) )
                    adj[i].push_back(j);

        memset(parent,-1,sizeof parent);
        int ans=max_match();
        printf("Case %d: %d\n",tt,ans);

    }
    return 0;
}
