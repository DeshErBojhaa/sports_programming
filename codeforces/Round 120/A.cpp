
#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;

int main()
{
    int N,tmp=0,total=0,neg=0;
    scanf(" %d",&N);
    vector<int >ans;
    for(int i=0;i<N;i++)
    {
        scanf(" %d",&tmp);
        total++;
        if(tmp<0) {neg++;}
        if(neg==3) {ans.push_back(total-1);neg=1;total=0;}



    }
    printf("%d\n",(int)ans.size());
    for(int i=0;i<(int)ans.size()-1;i++)
    printf("%d ",ans[i]);
    printf("%d\n",ans[ans.size()-1]);
}
