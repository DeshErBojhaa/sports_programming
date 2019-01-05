#include<stdio.h>
#include<algorithm>
#include<queue>
#include<string>
#include<map>
#include<iostream>
#include<vector>
#include<string.h>

using namespace std;

map<string,int>mp;
string baal;
char ball[22];
vector<int>vec[20009];
queue<int>Q;
//bool use[20009];
int indeg[20009];

int main()
{
    int T,edge;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
//        memset(use,false,sizeof use);
        memset(indeg,0,sizeof indeg);

        while(Q.size()) Q.pop();

        mp.clear();
        scanf(" %d",&edge);

        for(int i=0; i<(edge*2)+4; i++) vec[i].clear();

        int ind =0,bup,pola;

        for(int i=0; i<edge; i++)
        {
            scanf("%s",ball);
            baal=ball;

            if(mp[baal]==0)
                mp[baal]=++ind;

            bup=mp[baal];

            scanf("%s",ball);
            baal=ball;

            if(mp[baal]==0)
                mp[baal]=++ind;
            pola=mp[baal];

            vec[bup].push_back(pola);
            indeg[pola]++;
            ///printf("BUP %d  pola %d  INDEG %d => %d\n",bup,pola,pola,indeg[pola]);
        }
//printf("INDEX %d\n\n",ind);
        for(int i=1;i<=ind;i++)
        {if(indeg[i]==0) Q.push(i);}

        bool flag=true;  int cnt=0;

        while(Q.size())
        {
            int now=Q.front();
            Q.pop();
            cnt++;
//printf("NOW %d\n",now);
            for(int i=0;i<vec[now].size();i++)
            {
                int to=vec[now][i];
                if(indeg[to]==0)
                {
                    flag=false;
                    while(Q.size()) Q.pop();
                }
                if(indeg[to]>0) indeg[to]--;
                if(indeg[to]==0) Q.push(to);
            }
        }
//printf("COUNT %d\n",cnt);
        if ( (cnt)!=ind) flag=false;

        printf("Case %d: ",tt);
        if(flag) printf("Yes\n");
        else printf("No\n");

    }

    return 0;
}

/*

6
4
aa cc
bb cc
cc dd
dd bb
4
aa cc
bb cc
cc dd
dd cc
2
aa bb
cc dd
2
soda wine
water wine
3
soda wine
water wine
wine water

*/
