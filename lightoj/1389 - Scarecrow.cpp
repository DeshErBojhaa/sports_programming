#include<stdio.h>
#include<iostream>
#include<vector>
#include<string>
#include<string.h>

using namespace std;

int main()
{
    char ch;
    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        int n,flag=0;
        int ans=0;
        scanf(" %d",&n);
        for(int i=0;i<n;i++)
        {
            scanf(" %c",&ch);
            if(ch=='.' && flag==0)
            {
                ans++;
                flag=2;
            }
            else
            {
                flag--;
                if(flag<0) flag=0;
            }
        }
        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}
