#include<stdio.h>
#include<math.h>
#include<algorithm>
#include <iostream>
using namespace std;

const double pi=2*acos(0);

int main()
{
    int tc;
    scanf(" %d",&tc);
    double ans,hi,r1,r2,x1,x2,Y1,Y2,tri,sqr,dbc,pori,con_left,con_right,ark_left,ark_right;
    for(int tt=1; tt<=tc; tt++)
    {
        scanf(" %lf %lf %lf %lf %lf %lf",&x1,&Y1,&r1,&x2,&Y2,&r2);
        if(r1>r2)
        {
            swap(r1,r2);
            swap(Y1,Y2);
            swap(x1,x2);
        }
        dbc=sqrt(((x1-x2)*(x1-x2))+((Y1-Y2)*(Y1-Y2)));
        if((r1+r2)<=dbc) ans=0.0;
        else if(dbc+(r1)<=r2) ans=(pi*r1*r1);
        else
        {
            pori=((dbc+r1+r2)/2.0);
            tri=sqrt(pori*(pori-r1)*(pori-r2)*(pori-dbc));
            sqr=tri*2.0;
            hi=((tri*2.0)/dbc);
            con_left=(asin(hi/r1))*2.0;
            con_right=(asin(hi/r2))*2.0;
            ark_left=(pi*(r1*r1))*(con_left/(2.0*pi));
            ark_right=(pi*(r2*r2))*(con_right/(2.0*pi));
            ans=(ark_left+ark_right-sqr);
        }
        printf("Case %d: %.9lf\n",tt,ans);
    }
    return 0;
}
