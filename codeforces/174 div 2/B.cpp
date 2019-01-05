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

int main()
{
    string str;
    cin>>str;
    int a=0,f=0,i=0;

    for(int ii=0;ii<str.size();ii++)
    {
//        cout<<str[ii]<<endl;
        if(str[ii]=='A') a++;
        if(str[ii]=='F') f++;
        else if(str[ii]=='I')i++;
    }

    if(i==0) printf("%d\n",a);
    else if(i==1) printf("1\n");
    else printf("0\n");
}
