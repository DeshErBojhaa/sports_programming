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

bool arr[1009][1009];

bool check(int r, int c)
{
    for(int i=r;i<=r+2;i++)
    for(int j=c;j<=c+2;j++)
    {
        if(!arr[i][j]) return false;
    }
    return true;
}

int main()
{
    int n,m;
    scanf(" %d %d",&n,&m);
    bool flag=false;
    int ans=1<<24;
    for(int k=0;k<m;k++)
    {
        int r,c;
        scanf(" %d %d",&r,&c);
        arr[r][c]=true;
        for(int i=r-2;i<=r+2;i++)
        {
            for(int j=c-2;j<=c+2;j++)
            if(i>=0 && i<n && j>=0 && j<n && check(i,j) )
            {
                ans=min(ans,k+1); flag=true;
            }
        }
    }
    if(!flag) printf("-1\n");
    else printf("%d\n",ans);
    return 0;
}

