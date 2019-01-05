#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<map>
#include<string>
#include<queue>
#include<iostream>
#include<sstream>
#include<math.h>

using namespace std;

typedef long long ll;

const int inf=1<<30;
const double pi=2*(acos(0));
int n,m;
vector<int>adj[150];
int flag[150],a,b;

int main()
{
    scanf(" %d %d",&n,&m);

    for(int i=0;i<m;i++)
    {
        int frm,to;
         scanf(" %d %d",&frm,&to)   ;
         adj[frm].push_back(to);
         adj[to].push_back(frm);
    }

    for(int i=1;i<=n;i++)
    {
        if(flag[i]==0)
        {
            if(a>b) dfs()
        }
    }
    return 0;
}
