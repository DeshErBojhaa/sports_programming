#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<string>
#include<map>

using namespace std;

int T,arr[100001],n,C[100009],dpfor[100009],dpbac[100009],revarr[100009];

int bina(int low,int hi,int val)
{
    int mid;
    while(low<hi)
    {
        mid=(low+hi)/2;
        if(val>C[mid]) low=mid+1;
        else hi=mid;
    }
    return hi;
}

int main()
{
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {

        scanf(" %d",&n);

        for(int i=0;i<n;i++) {scanf(" %d",&arr[i]); revarr[n-i-1]=arr[i];}

        for(int i=1;i<=n;i++) C[i]=999999999;
        C[0]=-999999999;
        for(int i=0;i<n;i++)
        {
            int pos=bina(0,n,arr[i]);
            if(C[pos]>arr[i]) C[pos]=arr[i];
            dpfor[i]=pos;
        }

        for(int i=1;i<=n;i++) C[i]=999999999;
        C[0]=-999999999;

        for(int i=0;i<n;i++)
        {
            int pos=bina(0,n,revarr[i]);
            if(C[pos]>revarr[i]) C[pos]=revarr[i];
            dpbac[i]=pos;
        }

        int ans=-999999999;
        for(int i=0;i<n;i++)
            ans=max(ans,min(dpfor[i],dpbac[n-i-1]));

        printf("Case %d: %d\n",tt,ans*2-1);
    }
    return 0;
}
