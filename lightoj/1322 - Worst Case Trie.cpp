#include<stdio.h>
#include<iostream>
#include<algorithm>

using namespace std;

typedef long long ll;

const int mod=10000;
int arr[10001];

int main()
{
    arr[0]=1;
    arr[1]=2;
    arr[2]=5;

    for(int i=3;i<=10000;i++)
    {
        arr[i]=(arr[i-1]*i)+1;
        arr[i]%=mod;
    }
    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        int ind;
        scanf(" %d",&ind);
        if(ind<7)
        printf("Case %d: %d\n",tt,arr[ind]%mod);
        else printf("Case %d: %04d\n",tt,arr[ind%mod]%mod);
    }
    return 0;
}
