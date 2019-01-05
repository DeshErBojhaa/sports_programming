#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include<queue>

using namespace std;

int n,m,tot,chunk,ind,bad;
bool flag[101][101],chk[101];
vector<int>vec[101];

void dfs(int cur)
{
    chk[cur]=true;

    for(int i)



    return;

}

int main()
{
    cin>>n>>m;

    for(int i=0; i<n; i++)
    {
        scanf(" %d",&tot);
        if(tot==0) bad++;
        for(int j=0; j<tot; j++)
        {
            scanf(" %d",&ind);
            flag[i+1][ind]=true;
            flag[ind][i+1]=true;
        }
    }

    for(int i=1; i<=n; i++)
    {
        if(flag[i]==false)
        {
          //  cout<<"Call "<<i <<"  "<<j<<endl;
            chunk++;
            dfs(i);
        }
    }

    if(bad==n) cout<<n<<endl;
    else
    cout<<max(0,chunk-1)<<endl;


    return 0;
}
