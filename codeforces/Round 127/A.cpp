#include<stdio.h>
#include<string.h>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<stdlib.h>

using namespace std;

typedef long long ll;

int main()
{
    int point,time,A,B,la,lb;
    scanf(" %d %d %d %d %d %d",&point,&time,&A,&B,&la,&lb);

    bool flag=false;
    if(point==0) printf("YES\n");
    else
    {
        for(int i=0; i<time; i++)
        {
            for(int j=0; j<time; j++)
                if((A+B-(la*i)-(lb*j))==point || ((A+B)-(la*j)-(lb*i))==point || (A-(la*i)==point) || (B-(lb*i)==point ))
                {
                    flag=true;
                    break;
                }
        }
        if(flag) printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}

