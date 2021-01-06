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

int n,arr[200099];
bool flag[200099];
bool bad[200009]
long long yy,xx;

void find()
{
    yy=0;xx=1;
    int move=0;

    while(xx>0 && xx<=n)
    {
        //cout<<"xx "<<xx<<endl;
        flag[xx]=true;

        if(bad[xx]==true) {yy=-1;return;}

        yy+=arr[xx];

        if(move%2==0)
        xx+=(arr[xx]);  /// mind abs
        else
        xx-=(arr[xx]);



        move++;

        if( (xx>0 && xx<=n) )
        {
            if(flag[xx]==true)
            {
                yy=-1;
                return;
            }

        }
    }

}

int main()
{
    cin>>n;
    for(int i=2;i<=n;i++)
    scanf(" %d",&arr[i]);

    for(int i=1;i<n;i++)
    {
        memset(flag,false,sizeof flag);

        arr[1]=i;
        find();
        printf("%I64d\n",yy);
        if(yy!=-1)
        memset(bad,false,sizeof bad);
    }

    return 0;
}
