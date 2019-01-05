#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<iostream>

using namespace std;

struct data
{
    int to;
    double cost;
};
data tmp;
vector<data>vec[16];

int node,con,a,b;
double cst,dp[16][(1<<15)+6];

double rec(int cur,int mask)
{
    if(__builtin_popcount(mask)==node) return 0.0;

    double &ret=dp[cur][mask];
    if(ret>-0.5) return ret;
    int goable=0;
    int tot_go=vec[cur].size();
    double tmp=0.0;

    for(int i=0;i<tot_go;i++)
    {
        int to=vec[cur][i].to;

        if ( (mask&(1<<to))==0)
        {
            double val=rec(to,mask|(1<<to));
            if(val> -0.5)
            {
                goable++;
                tmp+=val+vec[cur][i].cost;
            }
        }
    }

    if(goable==0) return -1.0;

    if(goable>0) tmp+=5.0;
    ret=(tmp/(1.0*(goable)) );

    return ret;
}

int main()
{
    int T;
    cin>>T;
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d",&node,&con);
        for(int i=0;i<node;i++) vec[i].clear();

        for(int i=0;i<con;i++)
        {
            scanf(" %d %d %lf",&a,&b,&cst);
            tmp.cost=cst;
            tmp.to=b;
            vec[a].push_back(tmp);
            tmp.to=a;
            vec[b].push_back(tmp);
        }

        for(int j=0;j<16;j++) for(int i=0;i<=(1<<node);i++) dp[j][i]=-1.0;

        double ans=rec(0,1);
        printf("Case %d: %.8lf\n",tt,max(ans,0.000000));
    }
    return 0;
}
