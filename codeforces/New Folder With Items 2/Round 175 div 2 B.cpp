#include<stdio.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include<queue>
#include<string.h>
#include<string>
#include<sstream>
#include<math.h>
#include<map>

using namespace std;

vector<int>vec;
int N;
int main()
{
    cin>>N;

    for(int i=0;i<N;i++)
    {
        int tmp;
        scanf(" %d",&tmp);
        vec.push_back(tmp);
    }
    sort(vec.begin(),vec.end());

    long long ans=0;

    for(int i=0;i<vec.size();i++)
    {
        int soto,boro;
        soto=min(i+1,vec[i]);
        boro=max(i+1,vec[i]);

        ans+=abs(boro-soto);
    }
    cout<<ans<<endl;
    return 0;
}

