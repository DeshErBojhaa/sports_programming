#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<iostream>

using namespace std;

int dudh[1001];

int main()
{
    int T,n,bati;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        int low=1;
        int high=0,mid;
        scanf(" %d %d",&n,&bati);
        for(int i=0; i<n; i++)
        {
            scanf(" %d",&dudh[i]);
            high+=dudh[i];
        }

        while(low<=high)
        {
            mid=(low+high)/2;
            int tmp=0;
            int use=0;
            int flag=0;
            for(int i=0; i<n; i++)
            {
                if(use>=bati)
                {
                    flag=2;
                    break;
                }
                if(tmp+dudh[i]<=mid)
                    tmp+=dudh[i];
                else
                {
                    tmp=0;
                    use++;
                    i--;
                }
            }
            if(flag==0) /// batir size komao
            {
                high=mid-1;
            }
            else low=mid+1;
        }
        printf("Case %d: %d\n",tt,high+1);
    }
    return 0;
}
