#include<stdio.h>
#include<algorithm>
#include<iostream>

using namespace std;

long long node,m,inv,ans,arr[1000009],total;

int main()
{
    cin>>node>>m;

    for(int i=0;i<m;i++)
    {
        int a,b;
        scanf(" %d %d",&a,&b);
        arr[a]++;
        arr[b]++;
    }

    total=node*(node-1)*(node-2);
    total/=6;

    for(int i=1;i<=node;i++)
    {
        inv+=(arr[i]*(node-arr[i]-1));
    }
    inv/=2;

    cout<<total-inv<<endl;

    return 0;
}
