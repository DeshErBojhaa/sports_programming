#include<stdio.h>
#include<iostream>

using namespace std;

int need,dept,index,arr[1002];
double total;

int main()
{
    cin>>need>>dept>>index;

    for(int i=1; i<=dept; i++)
    {
        scanf(" %d",&arr[i]);
        total+=(arr[i]*1.0);
    }
    if((int)total<need)
    {
        cout<<"-1"<<endl;
        return 0;
    }

    double ans=1.0;

    for(int i=0; i<need-1; i++)
    {
        ans*=1.0*((1.0*((total-1)-(arr[index]-1)-i))/((1.0)*((total-1)-i)));
    }

    printf("%.9lf\n",1.0-ans);
    return 0;
}
