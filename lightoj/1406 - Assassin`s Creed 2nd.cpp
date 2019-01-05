#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string.h>
#include<iostream>

using namespace std;

vector<int>vec[16];
//bool flag[16][1<<16];
bool flag[1<<16];
int node,con,connected[1<<16],dp[1<<16];

void dfs(int cur,int mask)
{
    ///cout<<cur<<" ** "<<mask<<endl;
//    flag[cur][mask]=true;
        flag[mask]=true;
    connected[mask]=1;
    for(int i=0;i<vec[cur].size();i++)
    {
        int to=vec[cur][i];
     ///   cout<<to<<" ** "<<endl;
        if(!flag[(mask|(1<<to))])
            dfs(to,(mask|(1<<to)));
    }
    return ;
}

int rec(int mask)
{
    if(mask==0) return 0;
    int &ret=dp[mask];
    if(ret!=-1) return ret;
    ret=17;

    int use=mask;
    while(use>0)
    {
        if(connected[use]==1)
            ret=min(rec(mask^use)+1,ret);
        use--;
        use=use&mask;
    }
    return ret;
}

int main()
{
    int T;scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        memset(connected,0,sizeof connected);
        memset(dp,-1,sizeof dp);
        memset(flag,false,sizeof flag);
        for(int i=0;i<=node;i++) vec[i].clear();

        scanf(" %d %d",&node,&con);
        for(int i=0;i<con;i++)
        {
            int a,b;
            scanf(" %d %d",&a,&b);
            a--;b--;
            vec[a].push_back(b);
        }

///        for(int i=0;i<3;i++)
///        {
///            printf("%d  >>",i);
///            for(int j=0;j<vec[i].size();j++) printf(" %d",vec[i][j]); cout<<endl;
///        }
//int chodna=dfs(0,1);
        for(int i=0;i<node;i++)
        {memset(flag,false,sizeof flag);
            dfs(i,(1<<i));}

     ///   cout<<"DFS OK"<<endl;
        int ans=rec((1<<node)-1);
        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}
