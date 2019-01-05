#include<stdio.h>

int cover[200],nim[10009];

int main()
{
    int T,n,in,ans;
    for(int i=1; i<10001; i++)
    {
        for(int j=1; 2*j<i; j++)
        {
            int ck=nim[j]^nim[i-j];
            cover[ck]=i;
        }
        for(int j=0; j<201; j++)
            if(cover[j]!=i)
            {
                nim[i]=j;
                break;
            }
    }
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        scanf(" %d",&n);
        scanf(" %d",&ans);
        ans=nim[ans];
        for(int i=1; i<n; i++)
        {
            scanf(" %d",&in);
            ans=ans^nim[in];
        }
        if(ans==0) printf("Case %d: Bob\n",t);
        else printf("Case %d: Alice\n",t);
    }
    return 0;
}

