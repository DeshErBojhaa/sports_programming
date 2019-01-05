#include<stdio.h>

int nim(int n)
{
    if(n==1) return 0;
    if(n%2==0) return n/2;
    return nim((n-1)/2);
}

int main()
{
    int T,n,inp;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf(" %d",&n);
        int ans=0;
        for(int i=0;i<n;i++)
        {
            scanf(" %d",&inp);
            ans^=nim(inp);
        }
        if(ans) printf("Case %d: Alice\n",t);
        else printf("Case %d: Bob\n",t);
    }
    return 0;
}
