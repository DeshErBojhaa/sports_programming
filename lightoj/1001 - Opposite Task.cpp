#include<stdio.h>
int main()
{
    int tt;
    scanf("%d",&tt);
    for(int t=1; t<=tt; t++)
    {
        int in;
        scanf("%d",&in);
        if(in<=10) printf("0 %d\n",in);
        else printf("%d 10\n",in-10);
    }
    return 0;
}
