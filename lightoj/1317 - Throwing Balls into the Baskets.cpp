#include<stdio.h>

using namespace std;

int main()
{
    int T,n,m,k;
    double p;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf("%d %d %d %lf",&n,&m,&k,&p);
        printf("Case %d: %.8lf\n",tt,(1.0*n*k*p));
    }
    return 0;
}
