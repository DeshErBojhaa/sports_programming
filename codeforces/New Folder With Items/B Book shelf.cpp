#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>


using namespace std;

int n,dp[101][202][202],hor[101],var[101];

int rec(int cur,int vv,int hh)
{
    if(cur==n )
    {
        if(vv>=hh) return vv;
        return 1<<29;
    }

    int &ret=dp[cur][vv][hh];
    if(ret!=-1) return ret;
    ret=1<<29;

    if(hh+hor[cur]<=200)
        ret=min(ret,rec(cur+1,vv,hh+hor[cur]));

    ret=min(ret,rec(cur+1,vv+var[cur],hh));

    return ret;
}

int main()
{
    memset(dp,-1,sizeof dp);
    cin>>n;
    for(int i=0;i<n;i++) scanf(" %d %d",&var[i],&hor[i]);
    int ans=min(rec(0,0,0),999999999);
    cout<<ans<<endl;
    return 0;
}
