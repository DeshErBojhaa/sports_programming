#include<stdio.h>
#include<string.h>

using namespace std;

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        int ans=0,r,c,in;
        scanf(" %d %d",&r,&c);
        for(int i=0;i<r;i++)
           for(int j=0;j<c;j++)
           {
               scanf(" %d",&in);
               if((r-i+c-j-2)%2) ans=ans^in;
           }
        if(ans==0)    printf("Case %d: lose\n",t);
        else printf("Case %d: win\n",t);
    }
    return 0;
}
