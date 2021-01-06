#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>
#include<vector>
#include<queue>
#include<math.h>
#include<sstream>

using namespace std;

int main()
{
    int n,cnt=0;
    scanf(" %d",&n);

    for(int i=2;i<n;i++)
    {
        bool flag=true;
        for(int j=2;j<i;j++)
        {
            if(i%j==0) flag=false;
        }
        if(flag) cnt++;
    }
    printf("%d\n",cnt);
    return 0;
}
