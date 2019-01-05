#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<queue>
#include<iostream>
#include<math.h>

using namespace std;

struct matrix
{
    int mat[4][4];
};

int a,b,n,m,mod;
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
                ans.mat[i][j]=(ans.mat[i][j]+(a.mat[i][k]*b.mat[k][j]));
            }
        }
    }
    return ans;
}

matrix multiple(int po)
{
    matrix ans;
    if(po==1) return base;
    ans=multiple(po/2);
    ans=gunn(ans,ans);
    if(po%2) ans=gunn(ans,base);

    return ans;
}

int main()
{
    base.mat[0][0]=0;
    base.mat[0][1]=1;
    base.mat[0][2]=1;
    base.mat[0][3]=1;

    base.mat[1][0]=0;
    base.mat[1][1]=1;
    base.mat[1][2]=0;
    base.mat[1][3]=0;

    base.mat[2][0]=0;
    base.mat[2][1]=0;
    base.mat[2][2]=1;
    base.mat[2][3]=0;

    base.mat[3][0]=0;
    base.mat[3][1]=0;
    base.mat[3][2]=0;
    base.mat[3][3]=1;

    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
//        scanf(" %d %d %d %d",&a,&b,&n,&m);
        n=5;
        mod=pow(10,m);

        if(n==0) printf("Case %d: %d",tt,a);
        else
        {
            matrix basee=multiple(n-1);
            for(int i=0;i<4;i++)
            {
                for(int j=0;j<4;j++) cout<<basee.mat[i][j]<<" "; cout<<endl;
            }
            int ans=((basee.mat[0][0]*b)%mod+(basee.mat[0][1]*a)%mod)%mod;
            printf("Case %d: %d\n",tt,ans);
        }

    }
    return 0;
}




