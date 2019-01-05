#include<stdio.h>
#include<math.h>

const double pi= 2*acos(0);
int main()
{
    int tt;
    scanf("%d",&tt);
    double ax,ay,bx,by,lbc,lcd,lda;
    for(int t=1;t<=tt;t++)
    {
        double dhal,cy,dx,lab,lx,s,smalltri,hight,minasa,dy,cx,minasb;
        scanf("%lf %lf %lf %lf %lf %lf %lf",&ax,&ay,&bx,&by,&lbc,&lcd,&lda);
         lab=sqrt(((ax-bx)*(ax-bx))+((ay-by)*(ay-by)));
         lx=lab-lcd;
         s=(lx+lda+lbc)*.5;
         smalltri=sqrt(s*(s-lx)*(s-lbc)*(s-lda));
         hight=(2*smalltri)/lx;
         minasa=sqrt((lda*lda)-(hight*hight));
         dy=ay+hight;
         dx = ax-minasa;
         minasb=lx-minasa;
         dhal=(by-ay)/(bx-ax);
         cx=bx-minasb;
         cy=by+hight;
         printf("Case %d:\n",t);
//         printf("cx %lf cy %lf dx %lf dy %lf\n",cx,cy,dx,dy);


    }
    return 0;
}
