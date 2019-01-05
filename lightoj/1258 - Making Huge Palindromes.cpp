#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<algorithm>
#include<iostream>

using namespace std;

int par[2000009];
string str,a,b;

int pf(void)
{
    int k=0;
    for(int i=1;i<str.size();i++)
    {
        while(k>0 && str[i]!=str[k]) k=par[k-1];
        if(str[i]==str[k]) k++;
        par[i]=k;
    }

    return par[str.size()-1];
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=0;t<T;t++)
    {
        memset(par,0,sizeof par);
        cin>>a;
        b=a;
        reverse(a.begin(),a.end());
        str.clear();
        str+=a+'#'+b;

        int ball=pf();

        printf("Case %d: %d\n",t+1,2*b.size()-ball);
    }
    return 0;
}
