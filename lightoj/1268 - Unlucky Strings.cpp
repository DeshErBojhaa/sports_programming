#include<stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

typedef unsigned int ui;

struct matrix
{
    ui mat[52][52];
};
matrix base;

string chars,forbs;
int len,parent[55];

matrix multiplication(matrix a , matrix b)
{
    matrix ans;

    for(int i=0; i<len; i++)
    {
        for(int j=0; j<len; j++)
        {
            ans.mat[i][j]=0;
            for(int k=0; k<len; k++)
                ans.mat[i][j]=ans.mat[i][j]+(a.mat[i][k]*b.mat[k][j]);
        }
    }
    return ans;
}

matrix TakeToPower(int n)
{
    matrix ret,BASE;
    BASE=base;

    memset(ret.mat,0,sizeof ret.mat);

    for(int i=0; i<len; i++)
        ret.mat[i][i]=1;

    while(n)
    {
        if((n%2)==1)
            ret=multiplication(BASE,ret);
        n/=2;
        BASE=multiplication(BASE,BASE);
    }
    return ret;
}

void make_base()
{
    len=forbs.size();

    memset(base.mat,0,sizeof base.mat);
    memset(parent,0,sizeof parent);

    int k=0;
    for(int i=1; i<len; i++)
    {
        while(k>0 && forbs[i]!=forbs[k])
        {
            printf("Berore  K %d    I %d\n",k,i);
            k=parent[k-1];
            printf("JUMPING  %d\n",k);
        }
        if(forbs[i]==forbs[k]) k++;
        parent[i]=k;
        cout<<"************"<<endl;
    }

    return;
}

int main()
{
    int T,n;
    cin>>T;
    for(int tt=1; tt<=T; tt++)
    {
        cin>>n;
        cin>>chars>>forbs;

        make_base();
        matrix ans=TakeToPower(n);

        ui Ans=0;
        for(int i=0; i<len; i++) Ans+=ans.mat[0][i];

        printf("Case %d: ",tt);
        cout<<Ans<<endl;
    }
    return 0;
}

/*
1 1 0 0 0 0 0 0 0 0
1 0 1 0 0 0 0 0 0 0
0 0 1 1 0 0 0 0 0 0
1 0 0 0 1 0 0 0 0 0
1 0 0 0 0 1 0 0 0 0
0 0 1 0 0 0 1 0 0 0
1 0 0 0 0 0 0 1 0 0
1 0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0
*/
