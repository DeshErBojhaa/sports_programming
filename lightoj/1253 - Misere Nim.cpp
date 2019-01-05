#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int main()
{
    int T,in;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        int n,ans;bool flag=true;
        scanf(" %d",&n);
        scanf(" %d",&in);
        ans=in;
        for(int i=1; i<n; i++)
        {
            scanf(" %d",&in);
            if(in!=1) flag=false;
            ans=ans^in;
        }
        if(n==1) printf("Case %d: Bob\n",t);
        else
        {
            if(flag)
            {
                if(n%2) printf("Case %d: Bob\n",t);
                else printf("Case %d: Alice\n",t);
            }
            else
            {
                if(ans==0) printf("Case %d: Bob\n",t);
                else printf("Case %d: Alice\n",t);
            }
        }

    }
    return 0;
}
