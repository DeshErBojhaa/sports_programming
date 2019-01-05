#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<map>
#include<vector>
#include<queue>
#include<math.h>
#include<iostream>

using namespace std;

int main()
{

    string up,dn;
    cin>>up;
    cin>>dn;

    int pos=0;
    for(int i=0;i<dn.size();i++)
    {
        if(dn[i]==up[pos]) pos++;
    }
    printf("%d\n",pos+1);

    return 0;
}
