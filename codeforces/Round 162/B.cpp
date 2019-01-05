#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<math.h>

using namespace std;

int main()
{
    int n;
    int arr[200000];
    scanf(" %d",&n);

    int tmp,pre=0,go=0;
    for(int i=0;i<n;i++)
    {
        scanf(" %d",&arr[i]);

       // printf("dys %d\n",abs(pre-arr[i]));
        go+=abs(pre-arr[i]);
        pre=arr[i];
        go+=2;
    }

    printf("%d\n",go-1);


    return 0;
}

