#include<stdio.h>
#include<math.h>
#include<algorithm>

using namespace std;

int main()
{
    int T,n,inp,pos,neg;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        neg=0; pos=0;
        scanf(" %d",&n);
        for(int i=0;i<n;i++)
        {
            scanf(" %d",&inp);
            if(inp<0) neg++;
                pos+=abs(inp);
        }
        if(neg==n) printf("Case %d: inf\n",t);
        else
        {
            printf("Case %d: %d/%d\n",t,pos/(__gcd(pos,n-neg)),(n-neg)/(__gcd(pos,n-neg)));
        }
    }
    return 0;
}
