#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
#include<string>

using namespace std;

struct matrix
{
    int mat[31][31];
};
matrix base;

int T,n,lim,mod=10;

matrix gunn(matrix a,matrix b)
{
    matrix ans;

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            ans.mat[i][j]=0;
            for(int k=0; k<n; k++)
            {
                ans.mat[i][j]=(ans.mat[i][j]+(a.mat[i][k]*b.mat[k][j])%mod)%mod;
            }
        }
    }
    return ans;
}

matrix multiplication(int po)
{
    if(po==1) return base;
    matrix ret=multiplication(po/2);
    ret=gunn(ret,ret);
    if(po%2) ret=gunn(base,ret);

    return ret;
}

void make_base()
{
    memset(base.mat,0,sizeof base.mat);

    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            scanf(" %d",&base.mat[i][j]);

    return;
}

matrix jogg(matrix a,matrix b)
{
    matrix ans;

    for(int i=0;i<n;i++)
       for(int j=0;j<n;j++)
       ans.mat[i][j]=(a.mat[i][j]+b.mat[i][j])%10;

       return ans;
}

matrix abjab(int lim)
{
    if(lim==1) return base;

    int half=lim/2;
    matrix huda=abjab(half),midd,muda;

    if(lim%2)
    {
         midd=multiplication(half+1);
         muda=gunn(midd,huda);
         return jogg(jogg(huda,muda),midd);
    }
    else
    {
        midd=multiplication(half);
        muda=gunn(midd,huda);
        return jogg(huda,muda);
    }

}

int main()
{
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d",&n,&lim);
        make_base();

        matrix ans=abjab(lim);

        printf("Case %d:\n",tt);

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++) printf("%d",ans.mat[i][j]);
            printf("\n");
        }

    }
    return 0;
}

