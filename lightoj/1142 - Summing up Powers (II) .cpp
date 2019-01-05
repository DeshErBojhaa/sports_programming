#include<stdio.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<iostream>
#include<queue>

using namespace std;

typedef long long ll;

ll n,k,mal,matpow;

struct matrix
{
    ll mat[34][34];
};
matrix base;

int mod=10;

matrix gunn(matrix a,matrix b)
{
    matrix ans;

    for(int i=0; i<=30; i++)
    {
        for(int j=0; j<=30; j++)
        {
            ans.mat[i][j]=0;
            for(int k=0; k<=30; k++)
            {
                ans.mat[i][j]=(ans.mat[i][j]+(a.mat[i][k]*b.mat[k][j])%mod)%mod;
            }
        }
    }
    return ans;
}

matrix multiplication(ll po)
{
    if(po==1) return base;
    matrix ret=multiplication(po/2);
    matrix Ret=ret;
    ret=gunn(ret,ret);
    if(po%2) ret=gunn(base,ret);
     ret=gunn(ret,Ret);
    return ret;
}


int main()
{
    int tc;
    cin>>tc;
    for(int tt=1;tt<=tc;tt++)
    {
        memset(base.mat,0,sizeof base.mat);

        scanf(" %d %d",&n,&k);

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++) scanf("%d",&base.mat[i][j]);
        }

        //matpow=(ll)(k*(k+1))/2;
        matpow=k;
        matrix ans=multiplication(matpow);
        printf("Case %d:\n",tt);

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++) printf("%d",ans.mat[i][j]); cout<<endl;
        }

    }
    return 0;
}
