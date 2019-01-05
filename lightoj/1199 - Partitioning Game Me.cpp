#include<stdio.h>
#include<string.h>

int nim[10010];
bool flag[500];

void grundy()
{
    nim[0]=nim[1]=nim[2]=0;
    int i,j;
    for( i=3;i<=10010;i++)
    {
        memset(flag,false,sizeof flag);
        for( j=1;j*2<i;j++)
        {
            int x=j,y=i-j;
            flag[nim[x]^nim[y]]=true;
        }

        for( j=0;;j++) if(flag[j]==false) break;
        nim[i]=j;
    }

    return ;
}

int main()
{
    grundy();

    int T,n;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf(" %d",&n);
        int ans=0,tmp;
        for(int i=0;i<n;i++)
        {
            scanf(" %d",&tmp);
            ans^=nim[tmp];
        }
        if(ans) printf("Case %d: Alice\n",t);
        else printf("Case %d: Bob\n",t);
    }
    return 0;
}
