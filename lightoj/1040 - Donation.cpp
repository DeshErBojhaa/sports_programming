#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>

using namespace std;

struct data
{
    int f,t,c;
};

vector<data>v;
int n,no;
int arr[50][50], parent[51], rank[51];


void make_parent(int n)
{
    parent[n]=n;
    rank[n]=0;
}

int find_parent(int n)
{
    if(n!=parent[n]) return parent[n]=find_parent(parent[n]);
    return parent[n];
}

void joint(int x, int y)
{
    if(rank[x]>rank[y]) parent[y]=x;
    else
    {
        parent[x]=y;
        if(rank[x]==rank[y]) rank[y]++;
    }
}

bool com(data x, data y)
{
    return(x.c<y.c);
}

int mst(void)
{
    int ans=0;

    for(int i=0; i<n; i++)
        make_parent(i);

        for(int i=0; i<v.size(); i++)
        {
            int from=v[i].f;
            int to=v[i].t;
                if(find_parent(from)!=find_parent(to))
                {
                    no++;
                    joint(find_parent(from),find_parent(to));
                    ans+=v[i].c;
                }
        }
    return ans;
}

int main()
{
    int tc;
    scanf("%d",&tc);
    for(int tt=1; tt<=tc; tt++)
    {
        int total_cable=0, ans=0;;
        no=0;
        scanf(" %d",&n);
        int value;
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
            {
                scanf(" %d",&value);
                total_cable+=value;

                data tmp;
                tmp.f=i; tmp.t=j; tmp.c=value;
                if(value)
                v.push_back(tmp);
            }

        sort(v.begin(),v.end(),com);

        int bad=mst();
        if(no==(n-1))
        printf("Case %d: %d\n",tt,total_cable-bad);
        else
        printf("Case %d: -1\n",tt);
        v.clear();
    }
    return 0;
}
