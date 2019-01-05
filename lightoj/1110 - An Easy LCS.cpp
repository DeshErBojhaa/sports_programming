#include<stdio.h>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

string u,v;
string dp[101][101];

string Min_Max(string a, string b)
{
    if(a.size()==b.size()) if(a<b) return a ;
        else return b;
    if(a.size()>b.size()) return a;
    else  return b;
}

string rec(int a, int b)
{
    string p;
    if(a<0 || b<0) return "";
    string &ret=dp[a][b];
    if(ret!="-1") return ret;
    if(u[a]==v[b]) ret=rec(a-1,b-1)+u[a];
    else
    {
        ret=Min_Max(rec(a-1,b),rec(a,b-1));
    }
    return ret;
}

int main()
{
    string ans;
    int tt;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        cin>>u;
        cin>>v;
        int a=u.size()-1;
        int b=v.size()-1;
        for(int i=0; i<=max(a,b); i++)
            for(int j=0; j<=max(a,b); j++)
                dp[i][j]="-1";
        ans=rec(a, b);
        if(ans=="") printf("Case %d: :(\n",t);
        else{
        printf("Case %d: ",t);
        cout<<ans<<endl;
        }
        u.clear();
        v.clear();
    }
    return 0;
}
