
#include<cstdio>
#include<string.h>

int a[105][105],i,j,ss,x,k;
int main()
{
    scanf("%d",&x);
    memset(a,0,sizeof a);
    for (i=2;i<=100;i++)
      for (j=1;j<i;j++)
      {
          ss=0;
          for (k=1;k<j;k++)if (a[i][k]&&a[j][k])ss++;
          if (ss<=x)a[i][j]=a[j][i]=1,x-=ss;
      }
    puts("100");
    for (i=1;i<=10;i++,puts(""))
      for (j=1;j<=10;j++)printf("%d",a[i][j]);
    return 0;
}
