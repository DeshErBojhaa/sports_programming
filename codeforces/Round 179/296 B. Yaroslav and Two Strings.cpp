#include<stdio.h>
#include<iostream>
#include<string>

using namespace std;

typedef long long ll;

int n;
string up,dn;
ll mod=1000000007;
ll eQual,big,small,cnt;
int main()
{
    cin>>n>>up>>dn;
    big=(ll)1;small=(ll)1;eQual=(ll)1;
    ll total=1;

    for(int i=0;i<n;i++)
    {
        if(up[i]!='?' && dn[i]!='?')
        {
            eQual*=(ll)(up[i]==dn[i]);
            big*=(ll)(up[i]>=dn[i]);
            small*=(ll)(up[i]<=dn[i]);
        }
        if(up[i]=='?' && dn[i]=='?')
        {
            cnt+=2;

            eQual*=(ll)(10);
            big*=(ll)55;
            small*=(ll)55;
        }
        if(up[i]=='?' && dn[i]!='?')
        {
            cnt++;

            big*=(ll)(10-(dn[i]-'0') );
            small*=(ll)(1+(dn[i]-'0'));
        }
        if(up[i]!='?' && dn[i]=='?')
        {
            cnt++;

            big*=(ll)((up[i]-'0')+1);
            small*=(ll)(10-(up[i]-'0'));
        }

        big%=mod;
        eQual%=mod;
        small%=mod;

    }

    ll bad=(big-eQual+small+mod)%mod;

    for(int i=0;i<cnt;i++)
        total=(total*10)%mod;

    cout<<((((total-bad)%mod)+mod)%mod)<<endl;
    return 0;
}
