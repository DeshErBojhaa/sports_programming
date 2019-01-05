#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
#include<string.h>
#include<iostream>

using namespace std;

int no,ans,color[29][29][29];
string forb[50][3],aa,bb,cc,big,end;

bool chk(string str)
{
    bool flag;
    for(int i=0;i<no;i++)
    {
        flag=false;
        for(int j=0;j<forb[i][0].size();j++) if(forb[i][0][j]==str[0]) {flag=true;break;}
        if(flag)
        {
            flag=false;
            for(int j=0;j<forb[i][1].size();j++) if(forb[i][1][j]==str[1]) {flag=true;break;}
        }
        if(flag)
        {
            flag=false;
            for(int j=0;j<forb[i][2].size();j++) if(forb[i][2][j]==str[2]) {flag=true;break;}
        }
        if(flag) return false;
    }
    return true;
}

void make_flag(string str)
{
    int a,b,c;
    a=str[0]-'a';
    b=str[1]-'a';
    c=str[2]-'a';

}

int bfs(string inp)
{
    queue<string>Q;
    Q.push(inp);

    while(Q.size())
    {
        srting base=Q.front(); Q.pop();
        make_flag(base);
    }
}

int main()
{
    char hudai;
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%c",&hudai);

        cin>>big>>end;
        scanf(" %d",&no);
        for(int i=0;i<no;i++) {cin>>aa>>bb>>cc; forb[i][0]=aa; forb[i][1]=bb; forb[i][2]=cc;}
        memset(color,0,sizeof color);
        if(chk(big) && chk(end))
            ans=bfs(big);
        else ans=-1;
        printf("Case %d: %d\n",t,ans);
    }
    return 0;
}

