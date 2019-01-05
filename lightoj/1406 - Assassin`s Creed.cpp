#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>
#include<vector>

using namespace std;

int node,con,cango[16][16],dp[1<<15],pd[1<<15];
vector<int>vec[16];
bool flag[16];

void binar(int val)
{
    vector<int>vec;
    while(val>0)
    {
        if(val%2) vec.push_back(1);
        else vec.push_back(0);

        val/=2;
    }
    for(int i=vec.size()-1;i>=0;i--) printf("%d ",vec[i]);
    printf("\n");

    return;
}

void dfs(int cur)
{
    flag[cur]=true;
    for(int i=0;i<vec[cur].size();i++)
    {
        int to=vec[cur][i];
        if(flag[to]==false)
        {
            cango[cur][to]=1;
            dfs(to);
        }
    }
    return;
}

int min_visit(int msak)
{
    binar(msak);

    if(msak==0) return 0;
    int &rte=pd[msak];
    if(rte!=-1) return rte;
    rte=20;

    for(int row=1;row<=node;row++)
    {
        int match=true;
        for(int col=1;col<=node;col++)
        {
            if(cango[row][col]==1)
            {
                if((msak&(1<<col))==0)
                {
                    match=false; break;
                }
            }
        }
        if(match) {rte=1; break;}
    }

    return rte;
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
        int portion=(mask&(~use));
        int tmpans=min_visit(use)+rec(portion);
        ret=min(ret,tmpans);
        use--;
        use=(mask&use);
    }
    return ret;
}

int main()
{
    binar(1);
    binar(5);
    binar(13);
    binar(29);
    binar(31);
    binar(61);
    binar(127);
    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d",&node,&con);
        for(int i=0;i<con;i++)
        {
            int a ,b;
            scanf(" %d %d",&a,&b);
            vec[a].push_back(b);
        }
        memset(cango,0,sizeof cango);
        for(int i=1;i<=node;i++)
            memset(flag,false,sizeof flag),dfs(i);

        memset(dp,-1,sizeof dp);
        memset(pd,-1,sizeof pd);
        int ans=rec((1<<node)-1);
        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}
