#include<stdio.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<iostream>
#include<vector>

using namespace std;

string dp[15][1<<15],tmp;
string inf,add[15][15];
bool flag[15][1<<15];
int T,cs,n;
vector<string>vec;

string mmm(string a,string b)
{
    if((int)a.size()>(int)b.size()) return b;
    if((int)a.size()<(int)b.size()) return a;

    if(a<b) return a;
    return b;
}

void prepro()
{
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++) add[i][j]="";

    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
        {
            if(i==j) continue;
            string str=vec[j]+"#"+vec[i];
            string finaladd="";
            bool full_cont=false;
            int par[202];
            memset(par,0,sizeof par);
            int k=0;

            for(int ii=1; ii<str.size(); ii++)
            {
                while(k>0 && str[ii]!=str[k]) k=par[k-1];
                if(str[ii]==str[k]) k++;
                par[ii]=k;
                if(k==vec[j].size()) full_cont=true;
            }

            if(full_cont) finaladd="";
            else
            {
                int adno=par[str.size()-1];

                adno=vec[j].size()-adno;

                for(int ii=(vec[j].size()-adno); ii<vec[j].size(); ii++)
                    finaladd+=vec[j][ii];

            }

            add[i][j]=finaladd;
        }
    return;
}

string rec(int last,int mask)
{
    if(__builtin_popcount(mask)==n) return "";

    string &ret=dp[last][mask];
    if(flag[last][mask]) return ret;
    flag[last][mask]=true;
    ret=inf;

    for(int i=0; i<n; i++)
    {
        if((mask&(1<<i))==0)
        {
            string Add=add[last][i];
            if(Add=="")
                ret=mmm(ret,rec(last,(mask|(1<<i))));
            else
                ret=mmm(ret,Add+rec(i,(mask|(1<<i))));
        }
    }
    return ret;
}

int main()
{
    for(int i=0; i<403; i++) inf.push_back('Z');
    scanf(" %d",&T);
    for(cs=1; cs<=T; cs++)
    {
        vec.clear();
        scanf(" %d",&n);
        for(int i=0; i<n; i++)
        {
            cin>>tmp;
            vec.push_back(tmp);
        }
        prepro();
        string ans=inf;
        for(int i=0; i<n; i++)
        {
            memset(flag,false,sizeof flag);
            ans=mmm(ans,vec[i]+rec(i,(1<<i)));
        }

        printf("Case %d: ",cs);
        cout<<ans<<endl;
    }
    return 0;
}
