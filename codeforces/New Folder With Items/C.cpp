#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>

using namespace std;

double with,high,alfa,half,bad_with,rem_with,rem_with_with,bad1,bad2,bad_hi,rem_hi,rem_hi_hi;
 const double pi=2*acos(0);

double torad(double inp)
{
    return ((inp*pi)/180);
}



int main()
{
    //printf("%lf\n\n",sin(pi/2));
    scanf(" %lf %lf %lf",&with,&high,&alfa);

//    alfa=(alfa)%90.00;
    if(alfa>90.00) alfa=alfa-90.00;

    half=alfa/2;
    half=torad(half);  /// half is radiun
    alfa=torad(alfa);
//printf("ALF %lf\n\n",sin(alfa));
    bad_with=tan(half)*high;
//    printf("BAD WITH %lf\n",bad_with);
    rem_with=with-bad_with;
//    printf("REM_WITH %lf\n",rem_with);
printf("TAN %lf\n",tan(alfa));
    rem_with_with=rem_with/tan(half);

    bad1=(0.5*rem_with*rem_with_with);
    bad1=bad1*2;

    bad_hi=tan(half)*(with);
    rem_hi=high-bad_hi;
    rem_hi_hi=(rem_hi)/tan(half);

    bad2=(0.5*rem_hi*rem_hi_hi);
    bad2=bad2*2;

    double ans=(high*with)-(bad1+bad2);

    ans+=.000000001;

    printf("%.8lf\n",ans);


    return 0;
}
