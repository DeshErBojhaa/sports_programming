#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<queue>
#include<stdlib.h>

using namespace std;

int main()
{
    double ans;
    double n,total=0,tmp;
    scanf(" %lf",&n);
    for(int i=0;i<n;i++)
    {
        scanf(" %lf",&tmp);
        total+=tmp;
    }
    ans=total/n;
    printf("%.10lf\n",ans);
    return 0;
}
