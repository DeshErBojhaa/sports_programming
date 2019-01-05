#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

int dp[201][3][3];
string str;

int rec(int len,int left,int right)
{
    if(len==0) return 0;
    int &ret=dp[len][left][right];
    if(ret!=-1) return ret;
    ret=0;

    bool flag[202];
    memset(flag,false,sizeof flag);

    for(int i=1;i<=len;i++)
    {
        int ind=rec()
    }
}


int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        int left,right,low,high,ans=0;

        memset(dp,-1,sizeof dp);
        cin>>str;

        for(int i=0;i<str.size();i++)
        {
            left=right=0;

            if(i==0) left=0;
            if(str[i]=='X') left=1;
            if(i>0 && str[i-1]=='X' && str[i]=='X') left=2;

            if(str[i]=='.')
            {
                low=i;
                for(i=i;i<str.size();i++)
                if(str[i]=='X') break;
                i--;
                high=i;

                if(i+1==str.size()) right=0;
                if(i+1<str.size() && str[i+1]=='X') right=1;
                if(i+2<str.size() && str[i+1]=='X' && str[i+2]=='X') right=2;

                asn^=rec(high-low+1,left,right);
            }
        }
        if(ans) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
