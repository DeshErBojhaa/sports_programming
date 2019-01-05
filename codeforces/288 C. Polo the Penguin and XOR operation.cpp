#include<stdio.h>
#include<string.h>
#include<math.h>

using namespace std;

int n,flag[1000009];
long long total=0;

int find(int inp)
{
    int pos=0;
    int ret=0;

    while(inp)
    {
        if(inp%2==0)
        ret+=pow(2,pos);

        inp/=2;
        pos++;
    }
    return ret;
}

int main()
{
   // printf("%d %d %d %d\n\n\n",find(4),find(3),find(2),find(1));
    memset(flag,-1,sizeof flag);

    scanf(" %d",&n);

    for(int ii=n;ii>-1;ii--)
    {
        if(flag[ii]!=-1) continue;

        int index=find(ii);
        total+=(ii+ index);

        flag[ii]=index;
        flag[index]=ii;
    }

    printf("%I64d\n",2*total);
    for(int i=0;i<=n;i++) printf("%d ",flag[i]); printf("\n");
}
