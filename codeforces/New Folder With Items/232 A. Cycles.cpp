#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>

using namespace std;

int arr[100][100];

int main()
{
    int total;
    cin>>total;

    for(int i=2; i<100; i++)
    {
        for(int j=1; j<i; j++)
        {
            int cnt=0,k;
            for(k=1; k<j; k++)
            {
                if(arr[i][k] && arr[j][k]) cnt++;
            }
            if(cnt<=total)
            {
                arr[i][j]=arr[j][i]=1;
                total-=cnt;
            }
        }
    }
    cout<<"99"<<endl;

    for(int i=1; i<100; i++)
    {
        for(int j=1; j<100; j++) printf("%d",arr[i][j]);
        cout<<endl;
    }

    return 0;
}
