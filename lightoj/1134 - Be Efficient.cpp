#include<stdio.h>
#include<string.h>

int main()
{
    int T,n,mod,freq[100009],arr[100009];
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        memset(freq,0,sizeof freq);

        scanf(" %d %d",&n,&mod);
        for(int i=0;i<n;i++) scanf(" %d",&arr[i]);

        long long ans=0,rem=0;

        for(int i=0;i<n;i++)
        {
            rem=(rem+arr[i])%mod;
            ans+=freq[rem];
            if(rem==0) ans++;
            freq[rem]++;
        }
        printf("Case %d: %lld\n",t,ans);
    }
    return 0;
}
