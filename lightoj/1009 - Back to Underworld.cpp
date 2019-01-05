#include<stdio.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<string.h>

using namespace std;

#define po pop_back
#define pu push_back

bool flag[20003];
int a,b;
vector<int> V[20003];

void dfs(int i,bool sin)
{
      flag[i]=1;
    for(int j=0; j<V[i].size(); j++)
    {
        if(!flag[V[i][j]])
        {
            if(sin==0)
            {
                a++;
                dfs(V[i][j],1);
            }
            else if(sin==1)
            {
                b++;
                dfs(V[i][j],0);
            }
        }
    }
    return;
}

int main()
{
    int tt,fight,ans,x,y;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        scanf("%d",&fight);
        for(int i=1;i<=20000;i++)
        V[i].clear();
        int loop=-11;
        for(int i=1; i<=fight; i++)
        {
            scanf("%d %d",&x,&y);
            V[x].push_back(y);
            V[y].pu(x);
            loop=max(loop,max(y,x));
        }
        ans=0;
        a=0;
        b=0;
        memset(flag ,0, sizeof flag);
        for(int i=1; i<=loop+1; i++)
        {
            if(!flag[i] && V[i].size())
            {
                flag[i]=1;
                a++;
                dfs(i,true);
                ans+=max(a,b);
                a=0;
                b=0;
            }
        }
        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
/*
9
1 2
1 3
1 4
4 5
5 6
5 7
5 8
5 9
5 10



*/
