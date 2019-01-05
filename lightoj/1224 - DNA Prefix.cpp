#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<vector>

using namespace std;

struct data
{
    int ch[4];
    int pass,ans;
};

int n,N,ans;
data arr[1200009];
char str[51];

int find(char a)
{
    if(a=='A') return 0;
    if(a=='C') return 1;
    if(a=='G') return 2;
    if(a=='T') return 3;
}

void tri(int cur,int leaf)
{
    if(str[cur]=='\0') return ;
    int ind=find(str[cur]);

    if(arr[leaf].ch[ind]==-1)
    {
        arr[leaf].ch[ind]=++N;
    }
    int nextNode=arr[leaf].ch[ind];
    arr[nextNode].pass++;
    ans=max(ans,arr[nextNode].pass*(cur+1));
    tri(cur+1,nextNode);
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        scanf(" %d",&n);
        for(int i=0;i<1200009;i++)
        {
            memset(arr[i].ch,-1,sizeof arr[i].ch);
            arr[i].pass=0;
        }
        ans=0;
        N=0;
        for(int i=0; i<n; i++)
        {
            scanf("%s", str);
            tri(0,0);
        }
        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}
