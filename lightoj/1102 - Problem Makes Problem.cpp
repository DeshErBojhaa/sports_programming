#include<stdio.h>
#include<algorithm>
#include<math.h>

using namespace std;

long long f[2000009],n,k,mod=1000000007;

long long bm(long long n,long long p)
{
    if(p==0) return 1;
    long long ret=bm(n,p/2);
    ret=(ret*ret)%mod;
    if(p&1) ret=(ret*n)%mod;
    return ret;
}


int main()
{
    f[0]=1;
    for(int i=1;i<2000003;i++) f[i]=(f[i-1]*i)%mod;

    int T;
    scanf(" %d",&T);
    for(int i=0;i<T;i++)
    {
        scanf(" %d %d",&n,&k);
        long long lob=f[n+k-1];
        long long hor=(f[k-1]*f[n])%mod;
        hor=bm(hor,mod-2);
        long long ans=(lob*hor)%mod;
        printf("Case %d: %lld\n",i+1,ans);
    }

    return 0;
}
