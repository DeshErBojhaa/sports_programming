#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>

using namespace std;

long long mod,arr[200002],same;

int main()
{
    int n;
    cin>>n;

    for(int i=0;i<n;i++)
        cin>>arr[i];
    for(int i=n;i<2*n;i++)
    {
        cin>>arr[i];
        if(arr[i]==arr[i-n]) same++;
    }
    cin>>mod;

    sort(arr,arr+(2*n));
    int cnt=1;
    long long ans=1;

    for(int i=1;i<2*n;i++)
    {
        if(arr[i]==arr[i-1])
        {
            cnt++;
            ans*=cnt;

            while((ans%2==0) && same)
            {
                ans/=2;
                same--;
            }
            ans%=mod;
        }
        else
        cnt=1;
    }
    cout<<ans<<endl;

    return 0;
}
