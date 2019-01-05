#include <iostream>
#include <string>

using namespace std;

typedef long long ll;

const ll mod = 1000000007;

int main ()
{
    int n;
    cin >> n;
    string s1, s2;
    cin >> s1 >> s2;
    ll num = 0;
    ll bigger=1, lesser=1, equal=1;

    for (int i = 0; i < n; i++)
    {
        if (s1[i] == '?') num++;
        if (s2[i] == '?') num++;
        if (s1[i] != '?' && s2[i] != '?')
        {
            ///cout<<"Equal Mul  "<<(s1[i] == s2[i])<<endl;
            ///cout<<"Bigge Mul  "<<(s1[i] >= s2[i])<<endl;
            ///cout<<"Lesse Mul  "<<(s2[i] >= s1[i])<<endl;
            equal *= (ll)(s1[i] == s2[i]);
            bigger *= (ll)(s1[i] >= s2[i]);
            lesser *= (ll)(s2[i] >= s1[i]);
        }
        if (s1[i] == '?' && s2[i] != '?')
        {
            bigger *= (ll)(10-(s2[i]-'0'));
            lesser *= (ll)(s2[i]-'0'+1);
        }
        if (s1[i] != '?' && s2[i] == '?')
        {
            bigger *= (ll)(s1[i]-'0'+1);
            lesser *= (ll)(10-(s1[i]-'0'));
        }
        if (s1[i] == '?' && s2[i] == '?')
        {
            equal *= (ll)10;
            bigger *= (ll)55;
            lesser *= (ll)55;
        }
        equal %= mod;
        bigger %= mod;
        lesser %= mod;
    }
    ll bad = ((bigger+lesser-equal)%mod+mod)%mod;
    ll all = 1;
    for (int i = 0; i < num; i++)
        all = (all * 1ll * 10)%mod;
    cout << (all-bad+mod)%mod;
}
