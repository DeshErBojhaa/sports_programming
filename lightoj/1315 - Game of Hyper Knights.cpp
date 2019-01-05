#include<stdio.h>
#include<string.h>

int gr[800][800],movexx[]= {-2,-3,-2,-1,-1,1},moveyy[]= {1,-1,-1,-2,-3,-2};

int grundy(int x,int y)
{
    if(x<0 || y<0)return -1;
    int flag[10];
    memset(flag,0,sizeof flag);

    if(gr[x][y]!=-1) return gr[x][y];

    for(int i=0; i<6; i++)
    {
        int index=grundy(x+movexx[i],y+moveyy[i]);
        flag[index]=1;
    }
    int i;
    for( i=0;; i++)
        if(flag[i]==0) break;
    gr[x][y]=i;
    return gr[x][y];
}

int main()
{
    memset(gr,-1,sizeof gr);
    gr[0][0]=gr[0][1]=gr[1][0]=gr[1][1]=0;

    int ball=grundy(499,499),T,x,y;

    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        int ans=0,n;
        scanf(" %d",&n);
        for(int i=0;i<n;i++)
        {
            scanf(" %d %d",&x,&y);
            ans^=grundy(x,y);
        }
        if(ans) printf("Case %d: Alice\n",t);
        else printf("Case %d: Bob\n",t);

    }

    return 0;
}
