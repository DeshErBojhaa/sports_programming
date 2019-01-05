#include<stdio.h>
#include<vector>
#include<algorithm>
#include<queue>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

string str;
int up[400011],tree[400011];

void update(int root,int li,int ri,int left,int right)
{
    if(up[root])
    {
        if(li!=ri) up[root*2]=up[root*2+1]=1;
        up[root]=0;
        tree[root]+=(ri-li+1);
    }
    if(li>=left && ri<=right)
    {
        if(li!=ri) up[root*2]=up[root*2+1]=1;
        tree[root]+=(ri-li+1);
    }

    int mid=(li+ri)/2;
    update(root*2,li,mid,left,right);
    update(root*2+1,mid+1,ri,left,right);

    return;
}

int ans_print(int root,int left,int right,int n)
{
    if(up[root]==1)
    {
        tree[root]=+(right-left+1);
        if(left!=right) up[root*2]=up[root*2+1]=1;
    }

    if(left==right)
    {
        int val=str[left]-'0';
        return val+tree[root];
    }
    int mid=(left+right)/2;
    if(mid>=n) return ans_print(root*2,left,mid,n);
    else return ans_print(root*2+1,mid+1,right,n);
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int ii=1; ii<=T; ii++)
    {
        memset(up,0,sizeof up);
        str.clear();
        cin>>str;
        int q,from,to,node;
        scanf(" %d",&q);
        printf("Case %d:\n",ii);

        for(int x=0; x<q; x++)
        {
            char ch;
            scanf(" %c",&ch);
            if(ch=='I')
            {
                scanf(" %d %d",&from,&to);
                update(1,1,str.size(),from,to);
            }
            else
            {
                scanf(" %d",&node);
                printf("%d\n",ans_print(1,1,str.size(),node)%2);
            }
        }
    }
    return 0;
}
