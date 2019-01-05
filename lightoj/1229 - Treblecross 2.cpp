#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<iostream>
#include<vector>

using namespace std;

struct data
{
    int start,len;
};

vector<data> chunk;
int dp[202];

int rec(int len)
{
    if(len==0) return 0;
    if(len==1) return 1;

    int &ret=dp[len];
    if(ret!=-1) return ret;
    ret=0;

    bool flag[222];
    memset(flag,0,sizeof flag);

    for(int i=1; i<=len; i++)
    {
        int lrem=max(i-3,0);                 /// careful
        int rrem=max(0,len-(i+2));           /// careful

        int index=rec(lrem)^rec(rrem);
        flag[index]=true;
    }
    int i=0;
    for(i=0;; i++)
    {
        if(flag[i]==false)  break;
    }
    return ret=i;
}

int main()
{
    string str;
    vector<int>ans;
    memset(dp,-1,sizeof dp);
    int T;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        ans.clear();
        chunk.clear();

        int sum=0;

        cin>>str;

        bool flag=false;

        for(int i=0; i<=str.size()-3; i++)
        {
            int j=0;
            string s=str.substr(i,3);
            for( j=0; j<s.size(); j++)
                if(s[j]=='.')
                {
                    s[j]='X';
                    break;
                }
            if(s=="XXX")
            {
                ans.push_back(i+j+1);
                flag=true;
            }

        }

        if(flag)
        {
            ans.resize(unique(ans.begin(),ans.end())-ans.begin());
            sort(ans.begin(),ans.end());
            printf("Case %d:",t);
            for(int i=0; i<ans.size(); i++) printf(" %d",ans[i]);
            printf("\n");
            continue;
        }

        str="X.."+str+"..X";

        for(int i=0; i<str.size()-1; i++)  /// important
        {
            if(str[i]=='X')
            {
                int cnt=0,start=i+1;
                for(i=i+1; i<str.size(); i++)
                {
                    if(str[i]=='X') break;
                    else
                    cnt++;
                }
                i--;
                cnt=max(cnt-4,0);

                if(cnt)
                {
                    sum^=rec(cnt);    /// change this line after ac
                    data tmp;
                    tmp.start=start+2;
                    tmp.len=cnt;
                    chunk.push_back(tmp);
                }

            }
        }
        if(sum==0) printf("Case %d: 0\n",t);
        else
        {
            int now=0;
            //printf("CS %d\n",chunk.size());
            for(int i=0; i<chunk.size(); i++)
            {
                now=sum^rec(chunk[i].len);
                /// printf("sum %d\n",sum);
                for(int j=0; j<chunk[i].len; j++) /// careful
                {
                    int lrem=max(j-2,0);                 /// careful
                    int rrem=max(0,chunk[i].len-(j+3));  /// careful
                    /// printf("%d    %d\n",lrem,rrem)    ;
                    if((now^rec(lrem)^rec(rrem))==0) ans.push_back(chunk[i].start+j-2);
                }
            }

            printf("Case %d:",t);
            for(int i=0; i<ans.size(); i++) printf(" %d",ans[i]);
            printf("\n");
        }

    }
    return 0;
}
