#include<iostream>
#include<algorithm>
#include <stdio.h>

using namespace std;

typedef long long ll;

ll arr[100009];

int main()
{
    ll N,D;
    scanf(" %I64d %I64d",&N,&D);

    for(int i=0; i<N; i++)
        scanf(" %I64d",&arr[i]);

    ll ans=0;
    ll left=0;
    ll add=0;

    for(int i=2; i<N; i++)
    {
        while(arr[left]+D<arr[i]) left++;
        add=(i-left);
        ans+= ((add*(add-1))/2);
    }

    printf("%I64d\n",ans);

    return 0;
}
