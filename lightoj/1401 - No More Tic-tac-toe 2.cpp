#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<iostream>

using namespace std;

int dp[101][3][3],len;
string str;

int rec(int length,int left,int right)
{
    if(length==0) return 0;

    int &ret=dp[length][left][right];
    if(ret!=-1) return ret;
    ret=0;

    bool flag[101];
    memset(flag , false, sizeof flag);

    for(int i=1;i<=length;i++)
    {
        for(int j=1;j<3;j++)
        {
            if(i==1 && left==j) continue;
            if(i==length && right==j) continue;

            int ind=rec(i-1,left,j)^rec(length-i,j,right);
            flag[ind]=true;
        }
    }

    int i;
    for(i=0;;i++)
    if(flag[i]==false) break;
    return ret=i;
}


int main()
{
    int T,left,right,low,high;
    scanf(" %d",&T);
    memset(dp,-1,sizeof dp);
    for(int t=1;t<=T;t++)
    {
        int cnt=0,ans=0;
        cin>>str;
        len=str.size();
        for(int i=0;i<len;i++)
        {
            if(str[i]=='.')
            {
                low=i;
                for(i=i;i<len;i++)
                    if(str[i]!='.') break;
                i--;
                high=i;

                if(low==0) left=0;
                else if(str[low-1]=='X' ) left=1;
                else if(str[low-1]=='O') left=2;

                if(high==len-1) right=0;
                else if(str[high+1]=='X') right=1;
                else if (str[high+1]=='O')right=2;

              ///  cout<<endl<<"CALL "<<high-low+1<<" "<<left<<" "<<right<<endl;
                ans^=rec(high-low+1,left,right);
            }
            else cnt++;
        }

        if(cnt%2) ans=!ans;
        if(ans)
        printf("Case %d: Yes\n",t);
        else printf("Case %d: No\n",t);
    }
    return 0;
}
