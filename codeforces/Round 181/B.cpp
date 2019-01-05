#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<math.h>
#include<iostream>
#include<vector>
#include<queue>
#include<map>
using namespace std;

struct data
{
    int a,b,c;
};

vector<data>ans;
queue<int>Q;
int n,con;
vector<int>vec[101],tmpv;
bool inv=false;
bool flag[202];

void dfs(int cur,int cunt)
{
    // printf("==> %d %d\n",cur,cunt);
    if(cunt>3)
    {
        inv=true;
        return;
    }

    flag[cur]=true;

    for(int i=0; i<vec[cur].size(); i++)
    {
        int to=vec[cur][i];

        if(flag[to]==false)
        {
            tmpv.push_back(to);
            dfs(to,cunt+1);
        }
    }

    if(cunt==3 && inv==false)
    {
        data abal;
        abal.a=tmpv[0];
        abal.b=tmpv[1];
        abal.c=tmpv[2];

        ans.push_back(abal);
    }

    //printf("*** %d %d\n",cur,tmpv.size());
    if(cur==1 && tmpv.size()==3)
    {

        data abal;
        abal.a=tmpv[0];
        abal.b=tmpv[1];
        abal.c=tmpv[2];

        ans.push_back(abal);
    }
    if(tmpv.size()<3 && cunt==1)
    {
        // printf("Sz %d\n",(int)tmpv.size());
        for(int i=tmpv.size(); i<3 && Q.size(); i++)
        {
            //printf("DHUKSE\n");
            // printf("Pushing %d  Stat %d %d  ",Q.front(),cur,cunt);
            tmpv.push_back(Q.front());
            Q.pop();
            flag[tmpv[i]]=true;
        }

        data abal;
        abal.a=tmpv[0];
        abal.b=tmpv[1];
        abal.c=tmpv[2];

        ans.push_back(abal);

    }
    return;
}

int main()
{
    cin>>n>>con;

    if(con==0)
    {
        for(int i=1; i<=n-2; i++)
        {
            printf("%d %d %d\n",i,i+1,i+2);
            i++;
            i++;
        }
        return 0;
    }

    int indx=20;
    map<int,int>mp;
    vector<int>prio;

    for(int i=0; i<con; i++)
    {
        int a,b;
        scanf(" %d %d",&a,&b);
        mp[a]=indx++;
        mp[b]=++indx;
        vec[a].push_back(b);
        vec[b].push_back(a);
        prio.push_back(a);
        prio.push_back(b);
    }

    for(int i=1; i<=n; i++)
    {
        if(mp[i]==0)
        {
            Q.push(i);
        }
    }

    inv=false;
    for(int i=0; i<prio.size(); i++)
    {
        int use=prio[i];

        if(flag[use]==false && inv==false)
        {
            // printf("CALL Main %d\n",i);
            tmpv.clear();

            if(mp[use])
                tmpv.push_back(use);

            dfs(use,1);
        }
    }
    for(int i=1; i<=n; i++)
    {

        if(flag[i]==false && inv==false)
        {
            //printf("CALL Main %d\n",i);
            tmpv.clear();

            if(mp[i])
                tmpv.push_back(i);

            dfs(i,1);
        }
    }

    if(inv) printf("-1\n");
    else
    {
        map<data,int>aaa;
        int indxx=9;
        for(int i=0; i<ans.size(); i++)
        {
            data ball=ans[i];
            ///printf("dnfjnfjanfjanfjan");
            if(aaa[ball]==0)
            {
                aaa[ball]=++indxx;
                printf("%d %d %d\n",ball.a,ball.b,ball.c);
            }
        }
    }

    return 0;
}
