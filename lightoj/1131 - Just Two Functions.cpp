#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

struct matrix
{
    int mar[3][3];
};
matrix base;
int mod,a1,a2,b1,b2,c1,c2,f0,f1,f2,g0,g1,g2;

void make_base()
{

}

int main()
{
    int T,Q;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d %d %d %d %d %d %d %d %d %d %d %d %d",&a1,&b1,&c1,&a2,&b2,&c2,&f0,&f1,&f2,&g0,&g1,&g2,&mod,&Q);
        make_base();
        printf("Case %d:\n",tt);
        for(int q=0;q<Q;q++)
    }
    return 0;
}
