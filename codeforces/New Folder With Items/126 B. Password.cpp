#include<stdio.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<vector>
#include<iostream>

using namespace std;

string str;
int par[2000009],mm,len,maaa;
bool ok[2000009];

void kmp()
{
    len=str.size();int k=0;
    for(int i=1;i<len;i++)
    {
        while(k>0 && str[i]!=str[k])
            k=par[k-1];

        if(str[i]==str[k])    k++;
        par[i]=k;

        if(i!=len-1) ok[par[i]]=true;
    }
    return;
}

int main()
{
    cin>>str;
    kmp();
    //for(int i=0;i<7;i++) if(ok[i]) cout<<"1 ";else cout<<"0 "; cout<<endl;
    //cout<<par[len-1]<<endl;
    string ret="Just a legend";
    int Len=par[len-1];
    while(Len>0)
    {
        if(ok[Len])
        {
            ret=str.substr(0,Len);
            cout<<ret<<endl;
            return 0;
        }
        Len=par[Len-1];
    }
    cout<<ret<<endl;
    return 0;
}




