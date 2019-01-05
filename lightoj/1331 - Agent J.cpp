#include<stdio.h>
#include<math.h>
#include<stdlib.h>

using namespace std;

const double pi=2*(acos(0));
int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1;t<=tt;t++)
    {
        double r1,r2,r3;
        scanf("%lf %lf %lf",&r1,&r2,&r3);

        double a,b,c;
        a=r1+r2;
        b=r3+r2;
        c=r1+r3;

        double pori;
        pori=(a+b+c)/2;
//        printf("%lf %lf %lf %lf\n",a,b,c,pori);
        double area_tri;
        area_tri=sqrt(pori*(pori-a)*(pori-b)*(pori-c));
//        printf("area_tri %lf\n",area_tri);

       /// eiporjonto thik ase

        double ca,cb,cc;
        ca=acos(((a*a)+(c*c)-(b*b))/(2*a*c));
        cb=acos(((a*a)+(b*b)-(c*c))/(2*a*b));
        cc=acos(((c*c)+(b*b)-(a*a))/(2*b*c));
//        printf("ca %lf cb %lf cc %lf\n",ca,cb,cc);

        double area_a,area_b,area_c;
        area_a=(pi*(r1*r1))*(ca/(2*pi));
        area_b=(pi*(r2*r2))*(cb/(2*pi));
        area_c=(pi*(r3*r3))*(cc/(2*pi));
//        printf("ar_a %lf ar_b %lf ar_c %lf\n",area_a,area_b,area_c);

        double ans;
        ans=area_tri-(area_a+area_b+area_c);

        printf("Case %d: %.9lf\n",t,ans);
    }
    return 0;
}
