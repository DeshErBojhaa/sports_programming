#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

const int mod=1000000007;
int ncr[1001][1001],len,m,pos[1001],Left,Right;
vector<int>vec;
long long pow2=1,gunn=1,ans=1;

void NcR()
{
    for(int i=0;i<1001;i++)
        ncr[i][0]=1;
    ncr[1][1]=1;

    for(int i=2;i<1001;i++)
       for(int j=1;j<1001;j++)
        ncr[i][j]=(ncr[i-1][j]+ncr[i-1][j-1])%mod;

    return;
}

int main()
{
    cin>>len>>m;

    NcR();

    for(int i=0;i<m;i++)
        scanf(" %d",&pos[i]);

    sort(pos,pos+m);

    for(int i=1;i<m;i++)
    {
        int sofar=pos[i]-1-i;
        int position=pos[i]-pos[i-1]-1;
///        cout<<"SO F  "<<sofar<<"  pos  "<<position<<endl;
        ans=(ans* ncr[sofar][position])%mod;
///        cout<<"BF POW  "<<ans<<endl;
///        cout<<"POW  "<<(pos[i]-pos[i-1]-2)<<endl;
        for(int ii=1;ii<=(pos[i]-pos[i-1]-2);ii++)
        ans=(ans*2)%mod;
///        cout<<"ANS "<<ans<<endl;
    }
///    cout<<"last  "<<len-pos[m-1]<<endl;
    ans=(ans*  ncr[(len-m)][len-pos[m-1]])%mod;

    cout<<ans<<endl;
    return 0;
}
