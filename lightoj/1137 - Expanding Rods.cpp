#include<stdio.h>

#include<math.h>
const double pi=2*acos(0);
int main()
{
    double l,thib,thie,vv, ll,r,n,mid,c,con;
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        thib=0;
        thie=180;
        scanf("%lf %lf %lf",&l,&n,&c);
        ll=  (1+(n*c))*l;
        ll=ll+l;
        printf("ll %lf\n",ll);
        while((thie - thib)>.000001)
        {
            mid=(.5*(thib+thie));
            r=ll/mid;
            con=(.5*mid)*(pi/180);
            printf("connnn %lf\n",con);
            vv=2*sin(con)*r;
            if(vv-l>.0000001)
            {
                thib=mid;
            }
            else
            thie=mid;
        }
        //r=pi*(ll/mid);
        printf("final con %lf\n",mid);
        //printf("asn %lf\n",(ll*(cos(r))));
    }
    return 0;
}

/*

Sample Input

3
1000 100 0.0001
150 10 0.00006
10 0 0.001

Output for Sample Input

Case 1: 61.3289915
Case 2: 2.2502024857
Case 3: 0


*/

