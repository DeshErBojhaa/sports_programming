#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

string gens,dna,str;
int forward[100009],backward[100009],arr[100009],par[100009],strsize,genssize;

void kmp()
{
    memset(par,0,sizeof par);
    memset(arr,0,sizeof arr);
    int k=0;
    for(int i=1;i<strsize;i++)
    {
        while(k>0 && str[i]!=str[k]) k=par[k-1];
        if(str[i]==str[k]) k++;
        if(k==genssize) k=par[k-1];
        par[i]=k;
    }
    for(int i=0;i<str.size();i++) cout<<par[i]<<" "; cout<<endl;
    arr[0]=1;
    for(int i=1;i<genssize;i++)
    {
        if(par[i]==0) arr[i]=1;
        else arr[i]=arr[par[i]-1]+1;
    }
    for(int i=genssize;i<strsize;i++)
    {
        if(par[i]==0) arr[i]=0;
        else arr[i]=arr[par[i]-1];
    }
    return;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        memset(forward,0,sizeof forward);
        memset(backward,0,sizeof backward);

        cin>>dna>>gens;

        str=gens+'#'+dna;

        strsize=str.size();
        genssize=gens.size();

        kmp();
        for(int i=0;i<strsize;i++) forward[i]=arr[i];

        reverse(gens.begin(),gens.end());reverse(dna.begin(),dna.end()) ;
        str=gens+'#'+dna;

        kmp();
        for(int i=0;i<strsize;i++) backward[i]=arr[i];
        cout<<endl;
        for(int i=0;i<str.size();i++) printf("%d ",forward[i]); cout<<endl;
        for(int i=0;i<str.size();i++) printf("%d ",backward[i]); cout<<endl;

        long long ans=0;
        for(int i=genssize+1;i<strsize-1;i++)
        {
            ///cout<<"LUL "<<i<<" "<<str.size()-(i-gens.size()+1)<<endl;
            ans+=forward[i]*backward[strsize-(i-genssize+1)];
        }
        printf("Case %d: %lld\n",t,ans);
    }
    return 0;
}
