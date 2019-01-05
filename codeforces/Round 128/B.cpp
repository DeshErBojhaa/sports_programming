#include<stdio.h>
#include<string.h>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<stdlib.h>

using namespace std;

//typedef long long ll


long long arr[9999999];
int main()
{
    int tc;
    long long in;
     scanf(" %d",&tc);
    for(int i=0;i<tc;i++)
    {
        scanf(" %I64d",&arr[i]);

    }
    long long ans=0;
    for(int i=0;i<tc-1;i++)
    {
        if(arr[i]>arr[i+1])
        ans+=(arr[i]-arr[i+1]);
    }

    printf("%I64d\n",ans);
    return 0;
}
