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
//    cin>>str;
    int a=0,f=0,i=0,n;
    cin>>n;
    for(int ii=0;ii<n;ii++)
    {
        char ch;
        scanf(" %c",&ch);
        if(ch=='A') a++;
        if(ch=='F') f++;
        else if(ch=='I')i++;
    }

    if(i==0) printf("%d\n",a);
    else if(i==1) printf("1\n");
    else printf("0\n");
}

