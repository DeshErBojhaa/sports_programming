#include<stdio.h>
#include<iostream>

using namespace std;

typedef long long ll;
ll arr[110100];

int main()
{
    int T,n;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        ll low=1,high=0;
        scanf(" %d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf(" %d",&arr[i]);
            high+=arr[i];
        }

        while(low<high)
        {
            ll mid=(low+high)/2;
            ll life=mid;

            for(int i=1;i<=n;i++)
            {
                if(life<0) {break;}
                if((arr[i]-arr[i-1])>life) {life=-100;break;}
                if((arr[i]-arr[i-1])==life) {life--;}
            }
            if(life>0) high=mid;
            else low=mid+1;
        }
        printf("Case %d: %lld\n",tt,low);
    }
    return 0;
}
