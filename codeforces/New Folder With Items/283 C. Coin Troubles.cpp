#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

int n,m,tot,mod=1000000007,arr[309],adj[309],ans[5000009],cnt,indeg[309];

void dfs(int cur,int dep)
{
    cnt++;

    tot-=(dep*arr[cur]);
    if(tot<0) tot=-1;
    if(adj[cur])
    {
        dfs(adj[cur],dep+1);
        arr[cur]+=arr[adj[cur]];
    }

    return;
}

int main()
{
    cin>>n>>m>>tot;
    for(int i=1;i<=n;i++) scanf(" %d",&arr[i]);

    for(int i=0;i<m;i++)
    {
        int a,b;
        scanf(" %d %d",&a,&b);

        adj[b]=a;
        indeg[a]=b;
    }

    for(int i=1;i<=n;i++) if(indeg[i]==0)
    dfs(i,0);

    ans[0]=1;

    if(cnt!=n || tot<0) {cout<<"0"<<endl;return 0;}
    for(int i=1;i<=n;i++)
    {
        for(int j=0;j+arr[i]<=tot;j++)
        ans[j+arr[i]]=(ans[j+arr[i]]+ans[j])%mod;
    }

    cout<<ans[tot]<<endl;
    return 0;
}
