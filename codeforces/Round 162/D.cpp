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

int freq[100009];


int main()
{
    int n,use,boro=-1;
    scanf(" %d",&n);

    for(int i=0;i<n;i++)
    {
        scanf(" %d",&use);
        boro=max(boro,use);

        int lim=sqrt(use);

        for(int j=2;j<=(lim+1);j++)
        {
            if((use%j)==0)
            {

            }
        }
    }

    int ans=0;
    for(int i=2;i<=boro;i++)
    ans=max(ans,freq[i]);

    printf("%d\n",ans+1);

    return 0;
}
