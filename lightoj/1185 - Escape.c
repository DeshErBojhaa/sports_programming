#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<queue>
#include<vector>

using namespace std;

int node,edge,ans,flag[150],flog[150];
vector<int>vec[101];

bool chk(int pos,int idx)
{
    int wa=((idx+1)%2);

    if(wa==0)
    {
        if(flag[pos]==0)
        {
            flag[pos]=1;
            return true;
        }
        else return false;
    }
    if(wa==1)
    {
        if(flog[pos]==0)
        {
            flog[pos]=1;
            return true;
        }
        else return false;
    }
}

void bfs(int cr,int ind)
{
    queue<int>Q;
    Q.push(cr);
    Q.push(ind);

    while(Q.size())
    {
        int cur=Q.front();
        Q.pop();
        int index=Q.front();
        Q.pop();

        for(int i=0; i<vec[cur].size(); i++)
        {
            int to=vec[cur][i];

            if(chk(to,index))
            {
                Q.push(to);
                Q.push((index+1)%2);

                if((index+1)%2) ans++;
            }
        }
    }
    return;
}

int main()
{
    int T;
    scanf(" %d",&T);

    for(int tt=1; tt<=T; tt++)
    {
        scanf(" %d %d",&node,&edge);
        ans=0;

        for(int i=0; i<=node; i++)
            vec[i].clear();

        for(int i=0; i<edge; i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            vec[a].push_back(b);
            vec[b].push_back(a);
        }

        memset(flag,0,sizeof flag);
        memset(flog,0,sizeof flog);

        bfs(1,0);

        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}
