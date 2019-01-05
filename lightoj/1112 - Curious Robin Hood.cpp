#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

int tree[400009],arr[100009];

int make_tree(int n,int l,int r)
{
    if(l==r)
    {
        tree[n]=arr[l];
        return tree[n];
    }
    int mid=(l+r)/2;
    int p=make_tree(n*2,l,mid);
    int q=make_tree(n*2+1,mid+1,r);

    tree[n]=p+q;
    return p+q;
}

int sum(int n,int l,int r,int ll,int rl)
{
    if(r<ll || l>rl) return 0;
    if(l>=ll && r<=rl) return tree[n];

    int mid=(l+r)/2;
    int p=sum(n*2,l,mid,ll,rl);
    int q=sum(n*2+1,mid+1,r,ll,rl);

    return p+q;
}

int update(int n,int l,int r,int nd,int val)
{
    if(l==r)
    {
        if(val<0)
        {
            tree[n]=0;
            arr[l]=0;
        }
        else
        {
            tree[n]+=val;
            arr[l]+=val;
        }
        return tree[n];
    }
    int mid=(l+r)/2,p,q;
    if(mid>=nd)
    {
        p=update(n*2,l,mid,nd,val);
        q=tree[n*2+1];
    }
    else
    {
        p=tree[n*2];
        q=update(n*2+1,mid+1,r,nd,val);
    }
    tree[n]=p+q;
    return p+q;
}

int main()
{
    int T,n,m,ll,rl,nd,val,t;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        memset(arr,0,sizeof arr);
        memset(tree,0,sizeof tree);

        scanf(" %d %d",&n,&m);
        for(int i=1; i<=n; i++) scanf(" %d",&arr[i]);

        int ball=make_tree(1,1,n);

        printf("Case %d:\n",tt);
        for(int i=0; i<m; i++)
        {
            scanf(" %d",&t);
            if(t==3)
            {
                scanf(" %d %d",&ll,&rl);
                printf("%d\n",sum(1,1,n,ll+1,rl+1));
            }
            else if(t==2)
            {
                scanf(" %d %d",&nd,&val);
                ball=(update(1,1,n,nd+1,val));
            }
            else
            {
                scanf(" %d",&nd);
                printf("%d\n",arr[nd+1]);
                ball=update(1,1,n,nd+1,-111);

            }
        }
    }
    return 0;
}
