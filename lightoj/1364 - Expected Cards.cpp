#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;

double dp[16][16][16][16][3][3][3][3];
int A,B,C,D;

double rec(int a,int b,int c,int d,int ja,int jb,int jc,int jd,int cnt)
{
//    if(cnt==2) return 99;
    if(a>=A && b>=B && c>=C && d>=D) return a+b+c+d;
    double &ret=dp[a][b][c][d][ja][jb][jc][jd];
    if(ret>-0.5) return ret;
    ret=1.0;

    double aleft=13-a;  /// think about -ja
    double bleft=13-b;
    double cleft=13-c;
    double dleft=13-d;
    double jleft=2-(ja+jb+jc+jd);
    //printf("%.0lf\n",jleft);
    double totleft=(52+jleft-(a+b+c+d));
//printf("%.0lf %.0lf %.0lf %.0lf   %.0lf  %.0lf\n",aleft,bleft,cleft,dleft,jleft,totleft);
printf("%d %d %d %d **  %.0lf\n",a,b,c,d,totleft);

    ret+=rec(a+(a<13)?1:0,b,c,d,ja,jb,jc,jd,cnt+1)*(aleft/totleft);
    if(ja<2 && (ja+jb+jc+jd)<2)
    ret+=rec(a+(a<15)?1:0,b,c,d,ja+1,jb,jc,jd,cnt+1)*(jleft/totleft);

    ret+=rec(a,b+(b<13)?1:0,c,d,ja,jb,jc,jd,cnt+1)*(bleft/totleft);
    if(jb<2 && (ja+jb+jc+jd)<2)
    ret+=rec(a,b+(b<15)?1:0,c,d,ja,jb+1,jc,jd,cnt+1)*(jleft/totleft);

    ret+=rec(a,b,c+(c<13)?1:0,d,ja,jb,jc,jd,cnt+1)*(cleft/totleft);
    if(jc<2 && (ja+jb+jc+jd)<2)
    ret+=rec(a,b,c+(c<15)?1:0,d,ja,jb,jc+1,jd,cnt+1)*(jleft/totleft);

    ret+=rec(a,b,c,d+(d<13)?1:0,ja,jb,jc,jd,cnt+1)*(dleft/totleft);
    if(jd<2 && (ja+jb+jc+jd)<2)
    ret+=rec(a,b,c,d+(d<15)?1:0,ja,jb,jc,jd+1,cnt+1)*(jleft/totleft);

    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d %d %d",&A,&B,&C,&D);
        memset(dp,-1,sizeof dp);
        double ans=rec(0,0,0,0,0,0,0,0,0);
        if(A>15 || B>15 || C>15 || D>15) ans=-1;
        if(A+B+C+D>54) ans=-1;
        printf("Case %d: %.9lf\n",tt,ans);
    }
    return 0;
}
