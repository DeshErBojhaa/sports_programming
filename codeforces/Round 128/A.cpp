#include<stdio.h>
#include<string.h>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<stdlib.h>

using namespace std;

//typedef long long ll

struct data
{
    int index,fre;
};

int index;
int main()
{
    int tc;
    scanf(" %d",&tc);
    int in,ans=1<<30;
    data ba;
    ba.fre=0;

    for(int i=0;i<tc;i++)
    {
        scanf(" %d",&in);

        //arr[in]++;
        if(in<ans)
        {
            ba.fre=0;
            ans=in;
            ba.index=i+1;
        }
        else if(in==ans)
        ba.fre++;
//cout<<ans<<endl;
    }
    if(ba.fre>=1) printf("Still Rozdil\n");
    else
    printf("%d\n",ba.index);
    return 0;
}

