#include<stdio.h>
#include<vector>
#include<string.h>
#include<algorithm>

using namespace std;

struct pq
{
    int vertices,cost;
    pq(int first, int second)
    {
        vertices=first;
        cost=second;
    }
};

vector<pq> V[30005];
int cost1[30005];
int cost2[30005];
bool flag[30005];
int Max,seed,seeed;

void dddfs(int pita)
{
    flag[pita]=true;
    for(int i=0; i<V[pita].size(); i++)
    {
        if(!flag[V[pita][i].vertices])
        {
            cost2[V[pita][i].vertices]=cost2[pita]+V[pita][i].cost;
            dddfs(V[pita][i].vertices);
        }
    }
    return;
}

void ddfs(int abba)
{
    flag[abba]=true;
    for(int i=0; i<V[abba].size(); i++)
    {
        if(!flag[V[abba][i].vertices])
        {
            cost1[V[abba][i].vertices]=cost1[abba]+V[abba][i].cost;
            if(cost1[V[abba][i].vertices]>Max)
            {
                Max=cost1[V[abba][i].vertices];
                seeed=V[abba][i].vertices;
            }
            ddfs(V[abba][i].vertices);
        }
    }
    return;
}

void dfs(int bup)
{
    flag[bup]=true;
    for(int pola=0; pola<(int)V[bup].size(); pola++)
    {
        if(!flag[V[bup][pola].vertices])
        {
            cost2[V[bup][pola].vertices]=cost2[bup]+V[bup][pola].cost;
            if(cost2[V[bup][pola].vertices]>Max)
            {
                seed=V[bup][pola].vertices;
                Max=cost2[V[bup][pola].vertices];
            }
            dfs(V[bup][pola].vertices);
        }
    }
    return;
}

int main()
{
    int tt,nod,a,b,c;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
//        memset(flag,false,sizeof flag);
//        memset(flag,false,sizeof flag);


        memset(cost1,0,sizeof cost1);
//        memset(cost2,0,sizeof cost2);

        scanf("%d",&nod);
        for(int i=0; i<=nod+1; i++)
            V[i].clear();

        for(int i=0; i<nod-1; i++)
        {
            scanf(" %d %d %d",&a,&b,&c);
            V[a].push_back(pq(b,c));
            V[b].push_back(pq(a,c));
        }

        Max=0;
        memset(cost2,0,sizeof cost2);
        memset(flag,false,sizeof flag);
        dfs(0);

        Max=0;
        memset(cost1,0,sizeof cost1);
        memset(flag,false,sizeof flag);
        ddfs(seed);

//        Max=0;
        memset(cost2,0,sizeof cost2);
        memset(flag,false,sizeof flag);
        dddfs(seeed);
        printf("Case %d:\n",t);
        for(int i=0; i<nod; i++)
        {
            printf("%d\n",max((cost1[i]),cost2[i]));
        }

    }
    return 0;
}

/*

4
0 1 20
1 2 30
2 3 50
5
0 2 20
2 1 10
0 3 29
0 4 50
7
0 1 2303
3 5 5957
3 2 7732
0 2 163
4 0 1689
4 6 5156

*/
