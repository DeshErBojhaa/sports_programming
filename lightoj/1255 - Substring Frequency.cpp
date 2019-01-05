#include<stdio.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<iostream>

using namespace std;

string a,b,str;
int len,par[2000009];

int mf()
{
    memset(par,0,sizeof par);
    int k=0,ans=0;
    for(int i=1;i<len;i++)
    {
        while(k>0 && str[i]!=str[k])
            k=par[k-1];
        if(str[i]==str[k]) k++;
        par[i]=k;
        if(par[i]==b.size()) ans++;
    }
    return ans;
}


int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        cin>>a; cin>>b;
        str.clear();
        str=b+'#'+a;
        len=str.size();
        printf("Case %d: %d\n",t,mf());
    }
    return 0;
}
