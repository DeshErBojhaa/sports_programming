#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>

using namespace std;

int dp[51][7][5][2],len;
string str;

int rec(int cur,int fc,int fv,int x)
{
    if(fc>5) fc=5;
    if(fv>3) fv=3;

    if(cur==len)
    {
        if(x==0)
        {
            if(fc<5 && fv<3) return 1;
            else return 0;
        }
        if(x==1)
        {
            if(fc>=5 || fv>=3) return 1;
            else return 0;
        }
    }

    int &ret=dp[cur][fc][fv][x];
    if(ret!=-1) return ret;

    if(str[cur]=='?')
    {
        if(fv<3)
            ret=max(ret,rec(cur+1,fc+1,0,x));
        else
            ret=max(ret,rec(cur+1,fc+1,fv,x));
        if(fc<5)
            ret=max(ret,rec(cur+1,0,fv+1,x));
        else
            ret=max(ret,rec(cur+1,fc,fv+1,x));
    }

    if(str[cur]!='A' && str[cur]!='E' && str[cur]!='I' && str[cur]!='O' && str[cur]!='U')
     {
         if(fv<3)
            ret=max(ret,rec(cur+1,fc+1,0,x));
        else
            ret=max(ret,rec(cur+1,fc+1,fv,x));
     }
    else
    {
        if(fc<5)
            ret=max(ret,rec(cur+1,0,fv+1,x));
        else
            ret=max(ret,rec(cur+1,fc,fv+1,x));
    }

    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        str.clear();
        cin>>str;
        len=str.size();
        int s1=0,s2=0;

        memset(dp,-1,sizeof dp);
        s1=rec(0,0,0,0);

        s2=rec(0,0,0,1);

        if(s1==1 && s2==1) printf("Case %d: MIXED\n",t);
        if(s1==1 && s2==0) printf("Case %d: GOOD\n",t);
        if(s1==0 && s2==1) printf("Case %d: BAD\n",t);
    }
}
