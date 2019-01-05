#include<stdio.h>
#include<iostream>
#include<vector>
#include<string.h>
#include<iostream>
#include<algorithm>

using namespace std;

int len[1001];
vector<int>path,final_path;
int T,camp,night;

bool cango(int val)
{
    path.clear();
    int cnt=1;
    int sum=len[0];
    if(sum>val) return false;

    for(int i=1;i<=camp;i++)
    {
        sum+=len[i];
        if((camp-i+1)==(night-cnt) || sum>val)
        {
            path.push_back(sum-len[i]);
            sum=len[i];
            cnt++;
            if(sum>val || cnt>night) return false;
        }
    }
    if(sum>val) return false;
    path.push_back(sum);
    final_path=path;
    return true;
}

int main()
{
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        int low=1,high=0;
        scanf(" %d %d",&camp,&night);
        night++;
        for(int i=0;i<=camp;i++) {scanf(" %d",&len[i]);high+=len[i];}

        while(low<high)
        {
            int mid=(low+high)/2;
            if(cango(mid)) high=mid;
            else low=mid+1;
        }

        printf("Case %d: %d\n",tt,low);
        for(int i=0;i<final_path.size();i++) printf("%d\n",final_path[i]);
    }
    return 0;
}
