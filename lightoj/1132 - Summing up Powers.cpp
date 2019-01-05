#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

typedef long long ll;
typedef unsigned int ui;

struct matrix
{
    ui mat[54][54];
};
matrix base;

int T,K;
ll N;
ui comb[52][52];

matrix multiplication(matrix a,matrix b)
{
    matrix ans;

    for(int i=0; i<K+2; i++)
    {
        for(int j=0; j<K+2; j++)
        {
            ans.mat[i][j]=0;
            for(int k=0; k<K+2; k++)
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

    for(int i=0; i<K+2; i++)
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
    memset(base.mat,0,sizeof base.mat);

    base.mat[0][0]=0; base.mat[0][1]=1; base.mat[0][2]=1; base.mat[0][3]=1;
    base.mat[1][0]=0; base.mat[1][1]=1; base.mat[1][2]=0; base.mat[1][3]=0;
    base.mat[2][0]=0; base.mat[2][1]=0; base.mat[2][2]=1; base.mat[2][3]=0;
    base.mat[3][0]=0; base.mat[3][1]=0; base.mat[3][2]=0; base.mat[3][3]=1;
    return;
}

void combina()
{
    for(int i=0; i<51; i++) comb[i][0]=1;

    for(int i=1; i<51; i++)
        for(int j=1; j<=i; j++)
            comb[i][j]=comb[i-1][j]+comb[i-1][j-1];

    return;
}

int main()
{
    scanf(" %d",&T);
    combina();

    for(int tt=1; tt<=T; tt++)
    {
        cin>>N;
        K=2;
        //scanf(" %d",&K);
        make_base();

        matrix ans= TakeToPower(N);
        cout<<endl;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++) cout<<ans.mat[i][j]<<" ";
            cout<<endl;
        }
        printf("Case %d: ",tt);
        cout<<ans.mat[0][K+1]<<endl;
    }
    return 0;
}
