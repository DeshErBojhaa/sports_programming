#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include<queue>
#include<string.h>
#include<string>
#include<sstream>
#include<math.h>
#include<map>

using namespace std;

int N,K;

int main()
{
    scanf(" %d %d",&N,&K);

    for(int i=0;i<K;i++)
    {
        printf("%d ",N-i);
    }
    for(int i=1;i<=N-K;i++)
    printf("%d ",i);
    cout<<endl;
    return 0;
}
