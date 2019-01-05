#include<stdio.h>
#include<vector>
#include<queue>
#include<string.h>

using namespace std;
#define pu push_back
#define po pop_back

int city[1001];
int color[1001];
bool flag[1001];
vector<int > V[1005];


void bfs(int mm)
{
    int x;
    queue<int >Q;
    Q.push(mm);
    while(!Q.empty())
    {
        x=Q.front();
        Q.pop();
        for(int i=0; i<V[x].size(); i++)
            if(flag[V[x][i]]==0)
            {
                color[V[x][i]]+=1;
                flag[V[x][i]]=1;
                Q.push(V[x][i]);

            }
    }

    return;
}

int main()
{
    int tt,people,n_ct,con,x,y,temp,ans;
    scanf("%d",&tt);
    for(int yyy=1; yyy<=tt; yyy++)
    {
        memset(city, 0, sizeof city);
        scanf("%d %d %d",&people,&n_ct,&con);
        for(int z=0; z<n_ct+3; z++)
            V[z].clear();
        for(int p=1; p<=people; p++)
            scanf("%d",&city[p]);
        for(int c=1; c<=con; c++)
        {
            scanf("%d %d",&x,&y);
            V[x].pu(y);
        }

        ans=0;
        printf("Case %d:",yyy);
        memset(color ,0 , sizeof color);
        for(int p=1; p<=people; p++)
        {
            memset(flag ,0 , sizeof flag);
            color[city[p]]++;
            flag[city[p]]=1;
            bfs(city[p]);
        }
        for(int g=1; g<=n_ct; g++)
        {
            if(color[g]==people)
                ans++;
        }
        printf(" %d\n",ans);


    }

    return 0;
}
/*



2 4 4
2
3
1 2
1 4
2 3
3 4

3 6 9
2
4
5
1 3
1 2
4 2
2 3
3 6
6 4
4 5
5 1
5 6


*/
