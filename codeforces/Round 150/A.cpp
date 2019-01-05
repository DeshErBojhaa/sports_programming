#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<queue>
#include<map>
#include<string>
#include<iostream>
#include<sstream>
#include<math.h>

using namespace std;

int main()
{
    int n,k;
    scanf(" %d %d",&n,&k);

    map<int,int>use;
    use.clear();
    vector<int>V[100];
    for(int i=0; i<100; i++) V[i].clear();
    int inp;

    for(int i=0; i<k; i++)
    {
        scanf(" %d",&inp);
        use[inp]=i+1;
        V[i].push_back(inp);

    }

    for(int i=0; i<k; i++)
    {
        for(int j=1; j<=(n*k); j++)
            if(use[j]==0)
            {
                if(V[i].size()==n) continue;

                V[i].push_back(j);
                use[j]=(4444+j);
            }
    }

    for(int i=0; i<k; i++)
    {
        for(int j=0; j<V[i].size(); j++) printf("%d ",V[i][j]);
        printf("\n");
    }

    return 0;
}
