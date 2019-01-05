#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<queue>

using namespace std;

int N,mod=10007;

struct matrix
{
    int mat[4][4];
};
matrix base;

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
    if(po==1) return base;
    matrix ret=multiplication(po/2);
    ret=gunn(ret,ret);
    if(po%2) ret=gunn(base,ret);

    return ret;
}

void make_base()
{
    memset(base.mat,0,sizeof base.mat);

    base.mat[0][0]=1;base.mat[0][1]=1;base.mat[0][2]=1;base.mat[0][3]=1;
    base.mat[1][0]=1;
                     base.mat[2][1]=1;base.mat[2][3]=1;
                     base.mat[3][1]=1;
                     base.mat[3][2]=1;

    return;
}


int main()
{
    make_base();
    int T;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf(" %d",&N);

        matrix ans=multiplication(N);
//        printf("** %d %d %d %d\n",ans.mat[0][0],ans.mat[0][1],ans.mat[0][2],ans.mat[0][3]);
        int anss=(ans.mat[0][0])%mod;
        printf("Case %d: %d\n",tt,anss);

    }
    return 0;
}
