#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<math.h>
#include<iostream>

using namespace std;
int arr[1000009];
int ans[1000009];
int main()
{
    string str;

    cin>>str;


    int len=(int )str.size();
    int lft=len-1;
    int right=0;
    for(int i=0; i<str.size(); i++)
    {
        if(str[i]=='l')
        {
            arr[i]=lft;
            lft--;
        }
        else
        {
            arr[i]=right;
            right++;
        }


    }

    for(int i=0; i<str.size(); i++)
    {
        int idx=arr[i];
        ans[idx]=i+1;
    }

    for(int i=0; i<str.size(); i++) printf("%d\n",ans[i]);

    return 0;
}


