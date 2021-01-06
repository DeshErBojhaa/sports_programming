#include<stdio.h>
#include<iostream>
#include<algorithm>

using namespace std;

typedef long long ll;

const int mod=1000000007;

ll power(int base,int pp)
{
    ll ret=1;

    for(int i=0;i<pp;i++)
    {
        ret*=base;
        ret%=mod;
    }
    return ret;
}

int main()
{
    ll len,type,palin;
    ll ans=1;
    cin>>len>>type>>palin;

    if(palin==1 || palin>len)
    ans=power(type,len);
    else if(palin==len)
    ans=power(type,((len+1)/2));
    else
    {
        if(palin&1) ans=power(type,2);
        else ans=type;
    }
    cout<<ans<<endl;
    return 0;
}
