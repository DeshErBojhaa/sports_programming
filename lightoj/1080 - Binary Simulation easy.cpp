#include<stdio.h>
#include<iostream>
#include<string>

using namespace std;

int inp[100009],tree[400009];

void update(int root,int li,int ri,int l,int r)
{
    if(li>=l && ri<=r) {tree[root]=(tree[root]+1);return;}
    if(li>r || ri<l) return;
    int mid=(li+ri)/2;
    update(root*2,li,mid,l,r);
    update(root*2+1,mid+1,ri,l,r);
    return;
}

int sol(int cur,int l,int r,int n)
{
    int ans;
    if(l==r)
    {
        if(tree[cur]) ans=(inp[cur]+1)%2;
        else ans=inp[cur];
        return ans;
    }
    int mid=(l+r)/2;
    if(mid>=n)
    ans=sol(cur*2,l,mid,n);
    else ans=sol(cur*2+1,mid+1,r,n);
    return ans;
}

int main()
{
    int T,from,to,node;
    string str;
    char ch;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        cin>>str;
        for(int i=0; i<str.size(); i++)
            inp[i]=str[i]-'0';
        int q; scanf(" %d",&q);
        printf("Case %d:\n",t);
        for(int i=0; i<q; i++)
        {
            scanf(" %c",&ch);
            if(ch=='I')
            {
                scanf(" %d %d",&from,&to);
                update(1,1,str.size(),from,to);
            }
            else
            {
                scanf(" %d",&node);
                int ans=sol(1,1,str.size(),node);
                printf(":: %d\n",ans);
            }
        }

    }
    return 0;
}
