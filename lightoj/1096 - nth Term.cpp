#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

struct matrix
{
    int mat[4][4];
};
matrix base;

int n,a,b,c,mod=10007;

matrix gunn(matrix a,matrix b)
{
    matrix ans;

    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            ans.mat[i][j]=0;
            for(int k=0; k<4; k++)
            {
                ans.mat[i][j]=(ans.mat[i][j]+(a.mat[i][k]*b.mat[k][j])%mod)%mod;
            }
        }
    }
    return ans;
}

matrix multiplication(int po)
{
//    printf("PO %d\n",po);
    if(po==1) return base;
    matrix ret=multiplication(po/2);
    ret=gunn(ret,ret);
    if(po%2) ret=gunn(base,ret);
//    printf("\n\n");
//    for(int i=0;i<4;i++)
//    {
//        for(int j=0;j<4;j++)
//        printf("%d ",ret.mat[i][j]);
//        printf("\n");
//    }

    return ret;
}

void make_base()
{
    base.mat[0][0]=0;
    base.mat[0][1]=1;
    base.mat[0][2]=1;
    base.mat[0][3]=1;
    base.mat[1][0]=1;
    base.mat[1][1]=0;
    base.mat[1][2]=1;
    base.mat[1][3]=1;
    base.mat[2][0]=1;
    base.mat[2][1]=1;
    base.mat[2][2]=0;
    base.mat[2][3]=1;
    base.mat[3][0]=1;
    base.mat[3][1]=1;
    base.mat[3][2]=1;
    base.mat[3][3]=0;

    return;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d %d %d",&n,&a,&b,&c);


        make_base();
//matrix ba=gunn(base,gunn(base,base));

        matrix ball=gunn(base,base);
        ball=gunn(ball,ball);

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                printf("%d ",ball.mat[i][j]);
            }
            printf("\n");
        }

        if(n<=2) {printf("Case %d: 0\n",tt);continue;}
        matrix ans=multiplication(n-2);
//        for(int i=0;i<4;i++)
//        {
//            for(int j=0;j<4;j++) printf("%d ",ans.mat[i][j]);
//            printf("\n");
//        }

        printf("Case %d: %d\n",tt,(ans.mat[0][3]*c)%mod);
    }
    return 0;
}
