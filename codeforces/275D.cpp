#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;

const int lim=100009;
long long add[lim],sub[lim],val[lim];
bool flag[lim];

vector<int>vec[lim];

void dfs(int cur)
{
    flag[cur]=true;

    for(int i=0; i<vec[cur].size(); i++)
    {
        int to=vec[cur][i];

        if(flag[to]==false)
        {
            dfs(to);
            add[cur]=max(add[cur],add[to]);
            sub[cur]=max(sub[cur],sub[to]);
        }


    }

    long long value=val[cur]+add[cur]-sub[cur];
    if(value>0) sub[cur]+=value;
    else add[cur]-=value;

    return;

}

int main()
{
    int n;
    scanf(" %d",&n);
    for(int i=0; i<n-1; i++)
    {
        int a,b;
        scanf(" %d %d",&a,&b);
        vec[a].push_back(b);
        vec[b].push_back(a);
    }

    for(int i=1; i<=n; i++) scanf("%I64d",&val[i]);

    dfs(1);
    printf("%I64d\n",add[1]+sub[1]);
    return 0;
}
