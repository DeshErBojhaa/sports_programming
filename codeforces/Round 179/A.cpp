#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<math.h>
#include<stdlib.h>
#include<queue>
#include<vector>
#include<iostream>
#include<map>
#include<sstream>

using namespace std;

typedef long long ll;

int n;
string str;

map<int,int>mp;
int fre[2000];

int main()
{
    cin>>n;
    int ind=2;
    int ans=0;
    for(int i=0;i<n;i++)
    {
        int tmp;
        scanf(" %d",&tmp);

        fre[tmp]++;
    }

    int mmm=0;
    for(int i=1;i<2000;i++)
    mmm=max(mmm,fre[i]);

    if(n==1) {cout<<"YES"<<endl; return 0;}

    if(mmm<=(int) (n+1)/2) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;

    return 0;
}
