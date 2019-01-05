#include<stdio.h>
#include<algorithm>
#include<string.h>

using namespace std;

int main()
{
    int T,a,b,ans,dys1,dys2,dys[500];
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        int n;
        scanf(" %d",&n);
        memset(dys , 0, sizeof dys);

        for(int i=0;i<n;i++)
        {
            scanf(" %d %d",&a,&b);
            dys[i]=b-a-1;
        }
        ans=dys[0];
///        for(int i=0;i<n;i++) printf("%d ",dys[i]); printf("\n");
        for(int i=1;i<n;i++)
        {
            ans=ans^dys[i];
        }

        if(ans!=0) printf("Case %d: Alice\n",t);
        else printf("Case %d: Bob\n",t);
    }
    return 0;
}

