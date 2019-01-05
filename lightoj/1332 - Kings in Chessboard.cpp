#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>
#include<vector>

using namespace std;

struct matrix
{
    unsigned long long mat[36][36];
};

matrix base;
int N;
vector<pair<int,int> >vec;

matrix make_base()
{
    for(int i=0; i<36; i++)
        for(int j=0; j<36; j++)
            base.mat[i][j]=0;

    int i,j,k,c2=0,c1=0,l;

    for(i=0; i<10; i++)
    {
        for(j=i+2; j<10; j++)
        {
            c2=0;
            for(k=0; k<10; k++)
            {
                for(l=k+2; l<10; l++)
                {
                    if(abs(k-i)>1 && abs(k-j)>1 && abs(l-i)>1 && abs(l-j)>1)
                        base.mat[c1][c2]=1;
                    c2++;
                }
            }
            c1++;
        }
    }
    return base;
}

matrix gunn(matrix a,matrix b)
{
    matrix ans;
    for(int i=0; i<36; i++)
    {
        for(int j=0; j<36; j++)
        {
            ans.mat[i][j]=0;
            for(int k=0; k<36; k++)
            {
                ans.mat[i][j]=ans.mat[i][j]+(a.mat[i][k]*b.mat[k][j]);
            }
        }
    }
    return ans;
}

matrix multiple(int pow)
{
    if(pow==1) return base;
    matrix ans=multiple(pow/2);
    ans=gunn(ans,ans);
    if(pow%2) ans=gunn(base,ans);

    return ans;
}

int main()
{
    vec.clear();

    base=make_base();

    int T;
    for(int i=0;i<36;i++)
    {
        for(int j=0;j<36;j++) cout<<base.mat[i][j]; cout<<endl;
    }

    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        unsigned int anss=0;
        scanf(" %d",&N);
        if(N==1) anss=36;
        else
        {
            matrix ans=multiple(N-1);

            for(int i=0; i<36; i++)
                for(int j=0; j<36; j++)
                    anss+=ans.mat[i][j];

        }
        printf("Case %d: ",tt)   ;
        cout<<anss<<endl;
    }
    return 0;
}
