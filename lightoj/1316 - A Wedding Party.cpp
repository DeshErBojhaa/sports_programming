#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
#include<math.h>

using namespace std;

struct data
{
    int to,cost;
};
vector<data> v[502];
data tmp;

int n,m,s,sh[502],dp[502],nshop,pp[502][17];

int rec(int cur)
{
    if(cur==n-1) return sh[cur];
    int &ret=dp[cur];
    if(ret!=-1) return ret;
    ret=-1<<29;

    for(int i=0; i<v[cur].size(); i++)
    {
        int to=v[cur][i].to;
        ret=max(ret,rec(to)+sh[cur]);
    }
    return ret;
}

int findcost(int cur,int got)
{
///    printf(":: %d %d\n",cur,got);
    if(cur==n-1)
    {
        if(got+sh[cur]==nshop) return 0;
        else return 1<<29;
    }
    int &ret=pp[cur][got];
    if(ret!=-1) return ret;
    ret=1<<29;

    for(int i=0; i<v[cur].size(); i++)
    {
        ret=min(ret,findcost(v[cur][i].to,got+sh[cur])+v[cur][i].cost);
    }
    return ret;
}

int main()
{
    int T,has,f,to,c;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        scanf(" %d %d %d",&n,&m,&s);

        memset(sh,0,sizeof sh);
        memset(dp,-1,sizeof dp);
        memset(pp,-1,sizeof pp);

        for(int i=0; i<=n; i++) v[i].clear();

        for(int i=0; i<s; i++)
        {
            scanf(" %d",&has);
            sh[has]=1;
        }
        for(int i=0; i<m; i++)
        {
            scanf(" %d %d %d",&f,&to,&c);
            tmp.to=to;
            tmp.cost=c;
            v[f].push_back(tmp);
        }

        nshop=rec(0);
        if(nshop<0) printf("Case %d: Impossible\n",t);
        else
            printf("Case %d: %d %d\n",t,nshop,findcost(0,0));

    }
    return 0;
}

/*

6

5 5 2
0 3
0 1 10
1 2 10
0 3 50
2 3 10
3 4 10

7 8 4
1 3 5 6
0 1 10
2 1 10
2 3 10
0 3 10
3 6 10
3 5 10
5 4 10
6 4 10

7 8 4
1 3 5 6
0 1 10
2 1 10
2 3 10
0 3 10
3 6 10
5 3 10
4 5 10
6 4 10

5 5 3
1 2 3
0 1 10
1 2 10
2 4 10
4 3 10
3 1 10

*/
