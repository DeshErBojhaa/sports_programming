#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
#include<string>

using namespace std;

struct matrix
{
    int mat[6][6];
};
matrix base;

int T,inp,a1,b1,c1,a2,b2,c2,f0,f1,f2,g1,g2,g0,mod,Q;

matrix gunn(matrix a,matrix b)
{
    matrix ans;

    for(int i=0; i<6; i++)
    {
        for(int j=0; j<6; j++)
        {
            ans.mat[i][j]=0;
            for(int k=0; k<6; k++)
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

    base.mat[0][0]=(a1)%mod;
    base.mat[0][1]=(b1)%mod;
    base.mat[0][5]=(c1)%mod;
    base.mat[1][0]=1;
    base.mat[2][1]=1;
    base.mat[3][2]=(c2)%mod;
    base.mat[3][3]=(a2)%mod;
    base.mat[3][4]=(b2)%mod;
    base.mat[4][3]=1;
    base.mat[5][4]=1;

    return;
}

int main()
{
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d %d %d %d %d %d %d %d %d %d %d %d %d %d",&a1,&b1,&c1,&a2,&b2,&c2,&f0,&f1,&f2,&g0,&g1,&g2,&mod,&Q);

        make_base();

        printf("Case %d:\n",tt);
        for(int qq=0;qq<Q;qq++)
        {
            scanf(" %d",&inp);
            if(inp==0) {printf("%d %d\n",(f0)%mod,(g0)%mod);continue;}
            if(inp==1) {printf("%d %d\n",(f1)%mod,(g1)%mod);continue;}
            if(inp==2) {printf("%d %d\n",(f2)%mod,(g2)%mod);continue;}

            matrix ans=multiplication(inp-2);

            printf("%d %d\n",( (ans.mat[0][0]*f2)%mod+(ans.mat[0][1]*f1)%mod+(ans.mat[0][2]*f0)%mod+(ans.mat[0][3]*g2)%mod+(ans.mat[0][4]*g1)%mod+(ans.mat[0][5]*g0)%mod)%mod ,
                   ( (ans.mat[3][0]*f2)%mod+(ans.mat[3][1]*f1)%mod+(ans.mat[3][2]*f0)%mod+(ans.mat[3][3]*g2)%mod+(ans.mat[3][4]*g1)%mod +(ans.mat[3][5]*g0)%mod )%mod );
        }
    }
    return 0;
}
