#include<stdio.h>
#include<iostream>
#include<algorithm>

using namespace std;

typedef long long ll;

int arr[100009];

int main()
{
    int N;
    cin>>N;

    ll ans=0,tmp,pre=-99999999999,consi=1;
    cin>>pre;

    for(int i=1;i<N;i++)
    {
        scanf(" %I64d",&tmp);

        if(tmp==pre) consi++;
        else
        {
            ans+=((consi*(consi+1))/2);

            pre=tmp;
            consi=1;
        }
    }
    ans+=(consi*(consi+1))/2;
    cout<<ans<<endl;
    return 0;
}
