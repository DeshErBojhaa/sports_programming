#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int arr[101111],gass[404444];

int initialization(int n,int l,int r)
{
    if(l==r)
    {
        gass[n]=arr[r];
        return gass[n];
    }
    int mid=(l+r)/2;
    int p=initialization(n*2,l,mid);
    int q=initialization((n*2)+1,mid+1,r);
    gass[n]=min(p,q);
    return gass[n];
}

int find_solution(int n,int l,int r,int ll,int rl)
{
    if(r<ll || l>rl) return 1<<30;
    if(l>=ll && r<=rl) return gass[n];

    int mid=(l+r)/2;
    int p=find_solution(n*2,l,mid,ll,rl);
    int q=find_solution(n*2+1,mid+1,r,ll,rl);
    return min(p,q);
}

int main()
{
    int T,ll,rl,n,q;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        memset(arr,0,sizeof (arr));
        memset(gass,0,sizeof (gass));

        scanf(" %d %d",&n,&q);
        for(int i=1; i<=n; i++)
            scanf(" %d",&arr[i]);

        int ball=initialization(1,1,n);

        printf("Case %d:\n",tt);
        for(int i=0; i<q; i++)
        {
            scanf(" %d %d",&ll,&rl);
            printf("%d\n",find_solution(1,1,n,ll,rl));
        }
    }
    return 0;
}
