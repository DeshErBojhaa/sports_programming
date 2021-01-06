#include<stdio.h>
#include<iostream>

using namespace std;

typedef long long ll;

ll NcR[61][61];
ll male,fimale,total,ans;

void Make_combinations()
{
    for(int i=0;i<61;i++) NcR[i][0]=1;

    for(int i=1;i<61;i++)
        for(int j=1;j<=i;j++)
            NcR[i][j]=NcR[i-1][j]+NcR[i-1][j-1];

    return;
}

int main()
{
    Make_combinations();

    cin>>male>>fimale>>total;

    for(int i=4;i<=male;i++)
        for(int j=1;j<=fimale;j++)
            if(i+j==total) ans+=NcR[male][i]*NcR[fimale][j];

    cout<<ans<<endl;
    return 0;
}
