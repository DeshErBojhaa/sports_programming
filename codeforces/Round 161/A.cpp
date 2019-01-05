#include<stdio.h>
#include<algorithm>
#include<map>
#include<vector>
#include<math.h>


using namespace std;

int main()
{
    int arr[5][5],tmp,ans=0;


    for(int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
        {
            scanf(" %d",&tmp);

            if(tmp==1) ans=abs(j-2)+abs(i-2);
        }
    }
    printf("%d\n",ans);

    return 0;
}
