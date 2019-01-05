#include<stdio.h>
#include<queue>
#include<string.h>
#include<algorithm>
#include<vector>

using namespace std;

typedef pair<int,int> pii;

struct vertices
{
    int node,cost;
    vertices()
    {
        ;
    }
    vertices(int nd,int co)
    {
        node=nd;
        cost=co;
    }
};
vertices v_tmp;

struct data
{
    int node, cost;
    data()
    {
        ;
    }

    data(int no,int co)
    {
        node=no;
        cost=co;
    }
    bool operator<(const data &x)const
    {
        return cost>x.cost;
    }
};
data d_tmp;

int n_node,con,ss,inf=1<<30,dys[502][502],visited[18][1<<17],lpp;
vector<int>shop;
vector<vertices>adj[502];
pii dp[17][1<<17];

void clear_all()
{
    shop.clear();
    for(int i=0; i<=n_node; i++) adj[i].clear();
    return;
}

void dijkstra(int srs)
{

    for(int i=0; i<n_node; i++) dys[srs][i]=inf;
    dys[srs][srs]=0;

    priority_queue<data> Q;
    d_tmp.node=srs;
    d_tmp.cost=0;

    Q.push(d_tmp);

    while(Q.size())
    {
        int u,v,base_cost=0,go_cost=0;
        d_tmp=Q.top();
        Q.pop();

        u=d_tmp.node;

        base_cost=d_tmp.cost;

        for(int i=0; i<adj[u].size(); i++)
        {
            v=adj[u][i].node;
            go_cost=adj[u][i].cost;

            if(dys[srs][v]> go_cost+base_cost)
            {
                dys[srs][v]=go_cost+base_cost;
                d_tmp.node=v;

                d_tmp.cost=dys[srs][v];
                Q.push(d_tmp);
            }
        }
    }
    return ;
}

pii rec(int cur,int mask)
{
    if(cur==shop.size()-1) return make_pair(0,0);

    pii &ret=dp[cur][mask],ball;
    if(visited[cur][mask]==lpp) return ret;
    visited[cur][mask]=lpp;
    ret=make_pair(0,inf);

    for(int i=0;i<shop.size();i++)
    {
        if((mask & (1<<i))==0)
        {
            int u,v;
            u=shop[cur]; v=shop[i];
            if(dys[u][v]==inf) continue;

            ball=rec(i, mask | (1<<i));
            if(ball.second==inf) continue;
            ball.first++;
            ball.second+=dys[u][v];
            if(ball.first> ret.first) ret=ball;
            else if(ball.first== ret.first)
            {
                if(ball.second < ret.second) ret=ball;
            }

        }
    }
    return ret;
}


int main()
{
    int T,f,t,c,inp;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        lpp++;int bad=0;
        scanf(" %d %d %d",&n_node,&con,&ss);
        clear_all();
        for(int i=0; i<ss; i++)
        {
            scanf(" %d",&inp);
            shop.push_back(inp);
        }
        if(shop[0]!=0) {bad++; shop.push_back(0);}
        if(shop[shop.size()-1]!=n_node-1) {bad++; shop.push_back(n_node-1);}
        sort(shop.begin(),shop.end());

        for(int i=0; i<con; i++)
        {
            scanf(" %d %d %d",&f,&t,&c);
            adj[f].push_back(vertices(t,c));
        }


        for(int i=0; i<shop.size(); i++) dijkstra(shop[i]);
        pii ans=rec(0,0);

        if(ans.second>=inf) printf("Case %d: Impossible\n",tt);
        else printf("Case %d: %d %d\n",tt,ans.first-bad,ans.second);
    }
    return 0;
}
