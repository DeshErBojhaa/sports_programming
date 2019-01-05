#include<stdio.h>

int main()
{
    int T,n;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        double ans=0.0;
        scanf(" %d",&n);
        for(int i=1;i<=n;i++)
        ans+=(n/(i*1.0));
        printf("Case %d: %.8lf\n",tt,ans);
    }
    return 0;
}
