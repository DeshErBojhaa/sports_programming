#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>

using namespace std;

long long f[1000009];
const int mod=1000003;

long long bm(int a,int b)
{
    if(b==0) return 1;
    long long ret=bm(a,b/2);
    ret=(ret*ret)%mod;
    if(b&1) ret=(ret*a)%mod;
    return ret;
}

int main()
{
    f[1]=1; f[2]=2;
    for(int i=3;i<1000003;i++) f[i]=(f[i-1]*i)%mod;  /// okkkkk

    int T; scanf(" %d",&T);
    for(int t=0;t<T;t++)
    {
        int n,r;
        scanf(" %d %d",&n,&r);

        long long hor=(f[r]*f[n-r])%mod;
        long long d=1;
        d=bm(hor,mod-2)%mod;

        if(d==0)
        printf("Case %d: 1\n",t+1);
        else
        printf("Case %d: %lld\n",t+1,(f[n]*d)%mod);
    }
}
