#include<stdio.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<iostream>

using namespace std;

string str;
int dp[50][4][6][2][2][2],len;

int rec(int cur,int fv,int fc,int o,int g,int b)
{printf(":: %d %d\n",fv,fc);
    if(cur==len)
    {
        if(g==1 && b==1) return 3;
        else if(g==0 && b==1) return 2;
        else return 1;
    }

    int &ret=dp[cur][fv][fc][o][g][b];
      if(ret!=-1) return ret;



    if(str[cur]!='A' && str[cur]!='O' && str[cur]!='E' && str[cur]!='I' && str[cur]!='U' && str[cur]!='?')
    {fc++;fv=0;}
    else if(str[cur]=='?') {fc++;fv++;o=1;}
    else {fv++;fc=0;}

    if(fv==3 || fc==5)
    {printf("LUL %d %d\n",fv,fc);
        if(fv==3 && str[cur]!='?') {fv=1;fc=0;} else {fv=0;fc=0;}
        if(fc==5 && str[cur]!='?') {fc=1; fv=0;} else {fv=0;fc=0;}

        if(o==0)
        { printf("LUL\n");
            g=0;
            b=1;
        }

        if(o==1)
        {
            b=1; o=0;
        }
    }


    ret=rec(cur+1,fv,fc,o,g,b);
    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        str.clear();
        memset(dp,-1,sizeof dp);
        len=0;

        cin>>str;
        len=str.size();
        int ans=0;
        ans=rec(0,0,0,0,1,0);
        if(ans==1)
        printf("Case %d: GOOD\n",t);
        else if(ans==2)
        printf("Case %d: BAD\n",t);
        else
        printf("Case %d: MIXED\n",t);
    }
    return 0;
}
