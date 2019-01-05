#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include<queue>
#include<string.h>
#include<string>
#include<sstream>
#include<math.h>
#include<map>

using namespace std;

int n,str,end,cnt,go[100009];
bool flag[100009];

int main()
{
    scanf(" %d %d %d",&n,&str,&end);

    for(int i=1;i<=n;i++)
    scanf(" %d",&go[i]);

    cnt=0;

    int cur=str;
    while(1)
    {
        if(flag[cur]==true)
        {
            cnt=-1;
            break;
        }
        if(cur==end) break;
        flag[cur]=true;
        cnt++;
        cur=go[cur];
    }
    printf("%d\n",cnt);
}
