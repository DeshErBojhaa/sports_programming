#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include<string.h>

using namespace std;

vector<int>vec;
int arr[1000009];

int main()
{
    int T,N,tm;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        memset(arr,0,sizeof arr);
        vec.clear();
        scanf(" %d",&N);
        for(int i=0;i<N;i++)
        {
            scanf(" %d",&tm);
            arr[tm]++;
            arr[N-1-tm]++;
        }

        int flag=true;
        for(int i=0;i<N;i++)
        {
            if(arr[i]!=2) {flag=false;break;}
        }
        if(flag)
            printf("Case %d: yes\n",tt);
        else
            printf("Case %d: no\n",tt);
    }
    return 0;
}
