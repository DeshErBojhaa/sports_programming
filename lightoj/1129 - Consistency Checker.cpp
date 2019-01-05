#include<stdio.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<iostream>
#include<stdlib.h>

using namespace std;

struct data
{
    int cnt,ch[11],use;
};

char str[11];
data arr[100091];
int N;

bool tri(int cur,int leaf)
{
    if(str[cur]=='\0')
    {
        if(arr[leaf].use) return false;
        else
        {
            arr[leaf].cnt=1;
            return true;
        }
    }

    int idx=str[cur]-'0';
    if(arr[leaf].ch[idx]==0) arr[leaf].ch[idx]=++N;
    arr[leaf].use=1;
    if(arr[  arr[leaf].ch[idx]  ].cnt) return false;
    return tri(cur+1,arr[leaf].ch[idx]);
}

int main()
{
    int T,n;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        N=0;
        scanf(" %d",&n);

        bool flag=true;
        for(int i=0; i<=100090; i++)
        {
            arr[i].cnt=0;
            arr[i].use=0;
            memset(arr[i].ch,0,sizeof arr[i].ch);
        }

        for(int x=0; x<n; x++)
        {
            scanf("%s",str);
            if(flag) flag=tri(0,0);
        }
        if(flag) printf("Case %d: YES\n",t);
        else printf("Case %d: NO\n",t);
    }
    return 0;
}

/*

91
3
911
97625999
91125426
5
113
12340
123440
12345
98346
3
911
9
89
4
9
1
2
3
4
9
91
93
94
3
9111
9112
9113

*/
