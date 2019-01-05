#include<stdio.h>
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

string str;
vector<int> ans;
int dp[400];


int rec(int len)
{
//    printf(":: %d\n",len);
    if(len==0) return 0;
    if(len==1) return 1;

    int &ret=dp[len];
    if(ret!=-1) return ret;
    ret=0;

    bool flag[222];
    memset(flag,false,sizeof flag);

    for(int i=1; i<=len; i++)
    {
        int index=rec(i-1)^rec(len-i);
        flag[index]=true;
    }
    int i=0;
    for(i=0;; i++)
        if(flag[i]==false) break;
    return ret=i;
}

int main()
{
    int T;
    scanf(" %d",&T);
    memset(dp,-1,sizeof dp);
    for(int t=1; t<=T; t++)
    {
        ans.clear();
        cin>>str;
        int left,right,cnt=0;
        for(int i=0; i<str.size(); i++)
        {

            if(str[i]=='.')
            {
                cnt++;
                if(str[i-1]=='X' && str[i+1]=='X' && i>0 && i<str.size()-1)
                {
                    cout<<"1st "<<endl;
                    ans.push_back(i);
                }
                if(str[i-1]=='X' && str[i-2]=='X' && i>1)
                {
                    cout<<"2nd"<<endl;
                    ans.push_back(i);
                }

            }

            if(str[i]=='X' || i==str.size()-1)
            {
                cout<<"CNT "<<cnt<<endl;
                for(int k=1;k<=cnt;k++)
                if((rec(k-1)^rec(cnt-k))==0) {cout<<"pb "<<endl;ans.push_back(i-k);}
                cnt=0;
            }
        }
        printf("Case %d:",t);
        if(ans.size())
            for(int i=0; i<ans.size(); i++) printf(" %d",ans[i]);
        else
            printf(" 0");
        cout<<endl;
    }
    return 0;
}
