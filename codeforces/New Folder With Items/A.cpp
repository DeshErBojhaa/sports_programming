#include<string>
#include<iostream>
#include<stdio.h>
using namespace std;

int main()// 97   65
{
    printf("%d\n\n",8^3^5^7);
    string str;
    cin>>str;

    if(str[0]>='a' && str[0]<= 'z')
    str[0]=str[0]-32;
    cout<<str<<endl;
    return 0;
}
