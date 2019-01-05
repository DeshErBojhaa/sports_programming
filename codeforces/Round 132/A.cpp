#include<stdio.h>
#include<string>
#include<string.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<iostream>
#include<math.h>

using namespace std;

int main()
{
    int a,b;
    double up[100],dn[100];

    scanf(" %d",&a);

    for(int i=0; i<a; i++)
        scanf(" %lf",&up[i]);

    scanf(" %d",&b);
    for(int i=0; i<b; i++)
        scanf(" %lf",&dn[i]);

    double ratio=0;
    int ans=0;

    for(int i=0; i<a; i++)
    {
        for(int j=0; j<b; j++)
        {
           // printf("up %.1lf  dn %.1lf ",up[i],dn[j]);
            if(dn[j]/up[i]==floor(dn[j]/up[i]))
            {
                ans=max(ans,int(dn[j]/up[i]));
            }
        }
    }

    int count=0;
    for(int i=0; i<a; i++)
    {
        for(int j=0; j<b; j++)
            if(dn[j]/up[i]==ans)
                count++;
    }

    printf("%d",count);
    return 0;
}
