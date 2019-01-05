#include<stdio.h>
#include<string.h>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

#define pb push_back
#define mem(a,b) memset(a, b, sizeof (a))

vector<int>V[1001];
bool flag[1001];
int taka[1001];

bool bfs(int bup, int lok,int manush,int ave)
{
    flag[bup]=true;
    int mot_taka=0;
    queue<int>Q;
    mot_taka+=taka[bup];
    Q.push(bup);
    while(!Q.empty())
    {
        bup=Q.front();
        Q.pop();
        for(int j=0; j<V[bup].size(); j++)
        {
            if(!flag[V[bup][j]])
            {
                manush++;
                flag[V[bup][j]]=true;
                mot_taka+=taka[V[bup][j]];
                Q.push(V[bup][j]);
            }
        }
    }
    if((mot_taka%manush)==0)
    {
        if(mot_taka/manush==ave)
            return true;
    }
    else
        return false;
}

int main()
{
    int lok,first,second,con,total,ave,tt,manush;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        total=0;
        memset(taka,0, sizeof taka);
        mem(flag,0);
        scanf("%d %d",&lok,&con);
        for(int i=1; i<=lok; i++)
        {
            scanf("%d",&taka[i]);
            total+=taka[i];
        }
        for(int i=0; i<=lok; i++)
            V[i].clear();
        for(int i=1; i<=con; i++)
        {
            scanf(" %d %d",&first,&second);
            V[first].pb(second);
            V[second].pb(first);
        }
        if((total%lok)!=0)
            printf("Case %d: No\n",t);
        else
        {
            manush=0;
            ave=total/lok;
            bool potaka=true;
            for(int i=1; i<=lok; i++)
            {
                if(!flag[i])
                {
                    manush++;
                    potaka= bfs(i,lok,manush,ave);
                    manush=0;
                }
                if(!potaka)
                {
                    printf("Case %d: No\n",t);
                    break;
                }
            }
            if(potaka)
                printf("Case %d: Yes\n",t);
        }
    }

}
