#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<vector>

using namespace std;

struct data
{
    int frm, to, cost;
};

vector<data>v;
int n_h;
int parent[101], rank[101];    /// habi jabi declear;

bool com(data x, data y)
{
    return(x.cost<y.cost);
}

bool commm(data x, data y)
{
    return (x.cost>y.cost);
}

void make_parent(int node)
{
    parent[node]=node;
    rank[node]=0;
}

int find_parent(int node)
{
    if(node!=parent[node]) return parent[node]=find_parent(parent[node]);
    return parent[node];
}

void join(int f, int s)
{
    if(rank[f]>rank[s]) parent[s]=f;
    else
    {
        parent[f]=s;
        if(rank[f]==rank[s]) rank[s]++;
    }
    return;
}

int mst(void)
{
    for(int i=0; i<=n_h; i++)
        make_parent(i);

    int ans=0;

    for(int i=0; i<v.size(); i++)
    {
        int from=v[i].frm;
        int too=v[i].to;

        if(find_parent(from)!=find_parent(too))
        {
            join(find_parent(from),find_parent(too));
//            printf("parent[%d] %d  parent[%d] %d\n",from,parent[from],too,parent[too]);
//            printf("rank[%d] %d  rank[%d] %d\n",from,rank[from],too,rank[too]);
            ans+=v[i].cost;
        }
    }
    return ans;
}

int main()
{
    int t_c;
    scanf(" %d",&t_c);
    for( int tt=1; tt<=t_c; tt++)
    {
        int f,t,c;
        scanf(" %d",&n_h);

        while(scanf(" %d %d %d",&f,&t,&c)==3)
        {

            if(f==0 && t==0 && c==0) break;

            data tmp;
            tmp.frm=f;
            tmp.to=t;
            tmp.cost=c;

            v.push_back(tmp);

        }

        sort(v.begin(),v.end(),com);
        int ff=mst();
        for(int i=0;i<=n_h;i++)
//        printf("p %d\n",parent[i]);
//        printf("%d\n",ff);
        sort(v.begin(),v.end(),commm);
        int s=mst();
//        printf("%d\n",s);
        if((ff+s)%2)
            printf("Case %d: %d/2\n",tt,ff+s);
        else
            printf("Case %d: %d\n",tt,(ff+s)/2);

        v.clear();

    }
    return 0;
}
/*
4

2
0 1 5
0 1 2
0 1 6
1 2 9
0 2 2
0 0 0

1
0 1 10
0 1 20
0 0 0

3
0 1 99
0 2 10
1 2 30
2 3 30
0 0 0

2
0 1 10
0 2 5
0 0 0
*/
