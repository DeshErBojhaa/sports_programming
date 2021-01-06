#include<stdio.h>
#include<vector>
#include<iostream>

using namespace std;

vector<int>vec[100009];
bool flag[100009];

double dfs(int cur,int dep)
{
//    cout<<"** "<<cur<<"  "<<dep<<endl;
    flag[cur]=true;

    double ret=1/(dep*1.0);

    for(int i=0;i<vec[cur].size();i++)
    {
        int to=vec[cur][i];

        if(!flag[to])
        ret+=dfs(to,dep+1);
    }
    return ret;
}

int main()
{
    int n;
    cin>>n;

    for(int i=0;i<n-1;i++)
    {
        int a,b;
        cin>>a>>b;
        vec[a].push_back(b);
        vec[b].push_back(a);
    }
    double ans=dfs(1,1);
    printf("%.8lf\n",ans);
    return 0;
}
