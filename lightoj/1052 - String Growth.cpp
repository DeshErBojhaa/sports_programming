#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

typedef long long ll;
const ll mod=1000000007;


struct matrix
{
    ll mat[4][4];
};
matrix base;

ll fibo[45],N,M,X,Y,InitialB,InitialA,BigA,BigB,K,LilA,LilB,FinalAns;

matrix multiplication(matrix a,matrix b)
{
    matrix ans;

    for(int i=0; i<2; i++)
    {
        for(int j=0; j<2; j++)
        {
            ans.mat[i][j]=0;
            for(int k=0; k<2; k++)
            {
                ans.mat[i][j]=(ans.mat[i][j]+(a.mat[i][k]*b.mat[k][j])%mod)%mod;
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

    for(int i=0; i<2; i++)
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

void make_base()
{
    base.mat[0][0] = 0;   base.mat[0][1] = 1;
    base.mat[1][0] = 1;   base.mat[1][1] = 1;

    return;
}

int main()
{
    fibo[0]=0;
    fibo[1]=1;
    for(int i=2; i<=40; i++) fibo[i]=fibo[i-1]+fibo[i-2];

    int T;
    scanf(" %d",&T);

    for(int tt=1; tt<=T; tt++)
    {
        make_base();
        scanf(" %lld %lld %lld %lld %lld",&N,&X,&M,&Y,&K);
        if(N>M)
        {
            swap(N,M);
            swap(Y,X);
        }

        int dyst=M-N;
        if(dyst>40 || N>40 || M>40)
        {
            printf("Case %d: Impossible\n",tt);
            continue;
        }

        LilA=fibo[N];
        LilB=fibo[N+1];

        BigA=fibo[M];
        BigB=fibo[M+1];

        if(((Y*LilA)-(X*BigA))%((BigB*LilA)-(LilB*BigA)) !=0)
        {
            printf("Case %d: Impossible\n",tt);
            continue;
        }
        InitialB=((Y*LilA)-(X*BigA))/((BigB*LilA)-(LilB*BigA));

        if(((X-(LilB*InitialB))%LilA) !=0)
        {
            printf("Case %d: Impossible\n",tt);
            continue;
        }
        InitialA=(X-(LilB*InitialB))/LilA;

        if(InitialA<0 || InitialB<0)
        {
            printf("Case %d: Impossible\n",tt);
            continue;
        }

        matrix ans=TakeToPower(K);

        FinalAns=((ans.mat[1][0]*InitialA)%mod+(ans.mat[1][1]*InitialB)%mod)%mod;
        printf("Case %d: ",tt);
        cout<<FinalAns<<endl;
    }

    return 0;
}

