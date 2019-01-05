#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include <iostream>
#include<queue>

using namespace std;


vector<int>V[50003],vv;
int city_index[50003],parent[50003];
bool flag[50003];

void bfs(int start, int end)
{
    parent[start]=0;
    flag[start]=true;
    queue<int>Q;
    Q.push(start);
    while(Q.size())
    {
        int father=Q.front();
        Q.pop();
        for(int son=0; son<V[father].size(); son++)
        {
            if(!flag[V[father][son]])
            {
                flag[V[father][son]]=true;
                parent[V[father][son]] = father;
                if(V[father][son]==end)
                    return;
                Q.push(V[father][son]);
            }
        }
    }
    return;
}

int main()
{
    int test_case,total_visit;
    scanf(" %d",&test_case);
    for(int t=1; t<=test_case; t++)
    {
        scanf(" %d",&total_visit);
        memset(parent,0,sizeof parent);
        memset(city_index,0,sizeof city_index);

        int Max=-11;
        for(int i=1; i<=total_visit; i++)
        {
            scanf("%d",&city_index[i]);
            if(city_index[i]>Max)
                Max=city_index[i];
        }

        printf("Case %d:\n",t);

        for(int i=1; i<=Max+1; i++)
            V[i].clear();

        for(int i=1; i<total_visit; i++)
        {
            V[city_index[i]].push_back(city_index[i+1]);
            V[city_index[i+1]].push_back(city_index[i]);
        }

        for(int i=1; i<=total_visit; i++)
        {
            sort(V[city_index[i]].begin(),V[city_index[i]].end());
        }

        bfs(city_index[1],city_index[total_visit]);

        int pola=city_index[total_visit];

        while(pola!=city_index[1])
        {
            vv.push_back(pola);
            pola=parent[pola];
        }

        printf("%d",city_index[1]);

        for(int i=(vv.size())-1; i>=0; i--)
            printf(" %d",vv[i]);

        printf("\n");

        vv.clear();
        memset(flag,false,sizeof flag);
    }
    return 0;
}
