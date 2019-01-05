#include<stdio.h>

using namespace std;

int main()
{
    int T,b,s;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d",&b,&s);
        if(b%2) printf("Case %d: 0\n",tt);
        else  printf("Case %d: %.8lf\n",tt,1/(1.0*b+1));

    }
    return 0;
}
