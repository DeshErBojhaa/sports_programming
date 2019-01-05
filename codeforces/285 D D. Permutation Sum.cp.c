#include<algorithm>
#include<map>
#include<queue>
#include<vector>
#include<string.h>
#include<stdio.h>

using namespace std;

int n;
const int mod=1000000007;

map< pair<int,int> , int >mp;

int rec(int cur,int up,int get)
{
    if(cur>n) return n;

    if(mp[make_pair(up,get)]!=0) return mp[make_pair(up,get)];

    int ret=0;

    for(int i=1;i<=n;i++)
    {
        if( (up& (1<<i)) ==0 )
        {
            int new_get=((cur-1+i-1)%n+1);

            if(  (get& (1<<new_get)) ==0 )
            ret= (ret+rec(cur+1, (up|(1<<i)) , (get| (1<<new_get)))%mod )%mod;
        }
    }
    return mp[make_pair(up,get)]=ret;

}

int main()
{
    scanf(" %d",&n);
    int ans=rec(1,0,0);
    printf("%d\n",ans);
    return 0;
}
