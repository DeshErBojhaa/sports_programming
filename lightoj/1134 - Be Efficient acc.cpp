#include<stdio.h>
#include<string.h>

int main()
{
    int T,freq[100001];
    scanf(" %d",&T);

    for(int t=1;t<=T;t++)
    {
        int n,mod,tmp=0,inp;
        memset(freq,0,sizeof freq);
        scanf(" %d %d",&n,&mod);
        long long ans=0;

        for(int i=0;i<n;i++)
        {
            scanf(" %d",&inp);
            tmp+=inp;
            tmp=tmp%mod;
            ans+=freq[tmp];
            freq[tmp]++;
            if(tmp==0) ans++;
        }
        printf("Case %d: %lld\n",t,ans);
    }
    return 0;
}
