#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

int main()
{
    int T,up[101],down[101],n;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        memset(up,0,sizeof up);
        memset(down,0,sizeof down);

        scanf(" %d",&n);

        for(int i=0;i<n;i++) scanf(" %d",&up[i]);
        for(int i=0;i<n;i++) scanf(" %d",&down[i]);

        int ans=down[0]-up[0]-1;

        for(int i=1;i<n;i++)
        {
            ans=ans^(down[i]-up[i]-1);

        }

        if(ans==0) printf("Case %d: black wins\n",t);
        else printf("Case %d: white wins\n",t);
    }
    return 0;
}
