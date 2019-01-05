#include<stdio.h>

int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1;t<=tt;t++)
    {
        int n,p,q,e;
        scanf("%d %d %d",&n,&p,&q);
        int ans=0,w=0;int flag=0;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&e);
            if( w+e<=q && ans<p)
            {
                ans++; w+=e;
            }

        }
         printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
