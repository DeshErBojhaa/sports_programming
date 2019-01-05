#include<stdio.h>
#include<algorithm>

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        int cnt=0,idx,target,arr[111],n;
        scanf(" %d",&n);
        for(int i=1;i<=n;i++) scanf(" %d",&arr[i]);
        for(int i=1;i<=n;i++)
        {
            while(arr[i]!=i)
            {
                idx=arr[i];
                target=arr[idx];
                arr[idx]=idx;
                arr[i]=target;
                cnt++;
            }
        }
        printf("Case %d: %d\n",t,cnt);
    }
    return 0;
}
