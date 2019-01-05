#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
    double ans=1;
    int T,n;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        int subs=0;
        ans=1.0;
        scanf(" %d",&n);
        while(ans>0.5)
        {
            ans*=((1.0*(n-subs))/(n*1.0));
            subs++;
        }
        printf("Case %d: %d\n",tt,subs-1);
    }

    return 0;
}

