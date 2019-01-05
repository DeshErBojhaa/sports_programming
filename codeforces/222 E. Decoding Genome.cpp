#include<stdio.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<string>
#include<string.h>
#include<iostream>

using namespace std;

typedef long long ll;

ll len;
ll typ,k,mod=1000000007;

struct matrix
{
    ll mat[53][53];
};
matrix base;

matrix gunn(matrix a,matrix b)
{
    matrix ans;

    for(int i=0; i<53; i++)
    {
        for(int j=0; j<53; j++)
        {
            ans.mat[i][j]=0;
            for(int k=0; k<53; k++)
            {
                ans.mat[i][j]=(ans.mat[i][j]+( (a.mat[i][k]%mod)*(b.mat[k][j]%mod))%mod)%mod;
            }
        }
    }
    return ans;
}

matrix multiplication(ll po)
{
    if(po==1) return base;
    matrix ret=multiplication(po/2);
    ret=gunn(ret,ret);
    if(po%2) ret=gunn(base,ret);

    return ret;
}


int toint(char ch)
{
    if(ch>='a' && ch<='z')
    return (int)(ch-'a')+1;
    return (int) ch-'A'+27;
}

int main()
{
    char str[6];

    cin>>len>>typ>>k;

    for(int i=0;i<=typ;i++)
        for(int j=0;j<=typ;j++) base.mat[i][j]=1;

    for(int i=0;i<=typ;i++)  base.mat[i][0]=0;

    for(int i=0;i<k;i++)
    {
        scanf("%s",str);
        int a=toint(str[0]);
        int b=toint(str[1]);

        base.mat[a][b]=0;
    }

    matrix ans=multiplication(len);
    ll ret=0;

    for(int i=1;i<=typ;i++)
        ret=(ret+ans.mat[0][i])%mod;

    cout<<ret<<endl;
    return 0;
}
