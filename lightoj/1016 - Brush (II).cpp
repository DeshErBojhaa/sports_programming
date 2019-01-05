#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

vector<int>v;

int main()
{
    int T,n,x,y,w;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        v.clear();
        int ans=1;
        scanf(" %d %d",&n,&w);
        for(int i=0;i<n;i++)
        {
            scanf(" %d %d",&x,&y);
            v.push_back(y);
        }
        sort(v.begin(),v.end());
        int low=v[0];
        for(int i=1;i<v.size();i++)
        if(v[i]-w>low) {ans++;low=v[i];}
        printf("Case %d: %d\n",t,ans);
    }

    return 0;
}
