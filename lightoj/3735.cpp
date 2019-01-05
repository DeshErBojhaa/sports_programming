#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<string.h>
#include<string>

using namespace std;

typedef long long ll;
char tmp;

struct matrix
{
    int mat[102][102];
};
matrix base,tmpmat,usemat;

int Kk,Mm,Nn,par[60],length;

matrix multiplication(matrix a,matrix b)
{
    matrix ans;

    for(int i=0; i<length; i++)
    {
        for(int j=0; j<length; j++)
        {
            ans.mat[i][j]=0;
            for(int k=0; k<length; k++)
            {
                ans.mat[i][j]=(ans.mat[i][j]+(a.mat[i][k]*b.mat[k][j]));
            }
        }
    }
    return ans;
}

matrix TakeToPower(ll P)
{

    matrix R,Base;
    Base=base;
    memset(R.mat,0,sizeof R.mat);

    for(int i=0; i<length; i++)
        R.mat[i][i] = 1;

    while(P>0)
    {
        if(P%2==1)
        {
            R=multiplication(R,Base);
        }
        P/=2;
        Base=multiplication(Base,Base);
    }
    return R;
}

void addkoro(int ind)
{
    usemat=tmpmat;
    usemat.mat[ind][0]=1;
//    for(int i=0; i<length; i++)
//                {
//                    for(int j=0; j<length; j++) printf("%d ",usemat.mat[i][j]);
//                    cout<<endl;
//                }
//                cout<<endl;
    base=multiplication(base,usemat);
    return;
}

void khao(int ind)
{
    usemat=tmpmat;
    usemat.mat[ind][ind]=0;
//    for(int i=0; i<length; i++)
//                {
//                    for(int j=0; j<length; j++) printf("%d ",usemat.mat[i][j]);
//                    cout<<endl;
//                }
//                cout<<endl;
    base=multiplication(base,usemat);
    return;
}

void swapkoro(int ind1,int ind2)
{
    usemat=tmpmat;
    usemat.mat[ind1][ind1]=0;
    usemat.mat[ind1][ind2]=1;

    usemat.mat[ind2][ind2]=0;
    usemat.mat[ind2][ind1]=1;
//    for(int i=0; i<length; i++)
//                {
//                    for(int j=0; j<length; j++) printf("%d ",usemat.mat[i][j]);
//                    cout<<endl;
//                }
//                cout<<endl;

    base=multiplication(base,usemat);
    return;
}

int main()  /// N mane bilai koto  M mane pow koto  K mane kotogula instructions
{
    int tmpint,tmpint2;
    while(scanf(" %d %d %d",&Nn,&Mm,&Kk)==3)
    {
        if(Nn==0 && Mm==0 && Kk==0) break;
        length=Nn+1;
        for(int i=0; i<length; i++) tmpmat.mat[i][i]=base.mat[i][i]=1;

        for(int i=0; i<Kk; i++)
        {
            scanf(" %c",&tmp);
            if(tmp=='g')
            {
                scanf(" %d",&tmpint);
                addkoro(tmpint);
                for(int i=0; i<length; i++)
                {
                    for(int j=0; j<length; j++) printf("%d ",base.mat[i][j]);
                    cout<<endl;
                }
                cout<<endl;
            }
            else if(tmp=='e')
            {
                scanf(" %d",&tmpint);
                khao(tmpint);
                for(int i=0; i<length; i++)
                {
                    for(int j=0; j<length; j++) printf("%d ",base.mat[i][j]);
                    cout<<endl;
                }
                cout<<endl;
            }
            else
            {
                scanf(" %d %d",&tmpint,&tmpint2);
                swapkoro(tmpint,tmpint2);
                for(int i=0; i<length; i++)
                {
                    for(int j=0; j<length; j++) printf("%d ",base.mat[i][j]);
                    cout<<endl;
                }
                cout<<endl;
            }
        }

        for(int i=0; i<length; i++)
        {
            for(int j=0; j<length; j++) printf("%d ",base.mat[i][j]);
            cout<<endl;
        }
    }
    return 0;
}
