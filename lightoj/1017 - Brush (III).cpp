#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<map>
#include<vector>

using namespace std;

#define mp make_pair
#define pb push_back
#define pii pair<int,int>

int dp[101][101];
int n,w,k;

vector <pii> V;

int rec(int pass, int pos)
{
    if(pass>=k) return 0;
    if(pos>=V.size()) return 0;

    int &ret=dp[pass][pos];
    if(ret!=-1) return ret;

/// V[pos].first is Y cord;
/// V[pos].second is frequency of that Y cordinate

//    int dust=0;

    for(int j=pos; j<V.size(); j++)
    {
        int limit=V[j].first+w;
        int i,dust=0;
        for( i=j; i<V.size() && V[i].first<=limit ; i++)
            dust+=V[i].second;
//        printf("zz %d %d\n",pass,dust);
        ret=max(ret,rec(pass+1,i)+dust);
//        ret=max(ret,rec(pass,pos+1));
    }
    return ret;
}

int main()
{
    int tt,x,y;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        map<int,int> Map;
        map<int,int>:: iterator it;

        scanf(" %d %d %d",&n,&w,&k);
        for(int i=0; i<n; i++)
        {
            scanf(" %d %d",&x,&y);
            Map[y]++;
        }

        V.clear();
        for(it=Map.begin(); it!= Map.end(); it++)
            V.pb(mp((*it).first,(*it).second));

        sort(V.begin(),V.end());

        memset(dp,-1,sizeof dp);

        int ans=rec(0,0);
        printf("Case %d: %d\n",t,ans);

    }
    return 0;
}

/*
5 4 3
0 0
12 3
12 4
12 5
12 44

5 4 2
0 0
12 3
12 4
12 5
12 44

3 2 1
0 0
20 2
30 2

3 1 1
0 0
20 2
30 2
*/

