#include<stdio.h>
#include<string.h>
char grid[21][21];
int ans;
const int mrow[]={-1,0,1,0};
const int mcol[]={0,1,0,-1};
int dfs(int i,int j,int maxrow,int maxcol)
{
    int r,c;
    for(int z=0;z<=3;z++)
    {
        r=i+mrow[z];
        c=j+mcol[z];
        if(r>0 && c >0 && r<=maxrow && c<=maxcol && grid[r][c]=='.')
        {
            ans++;
            grid[r][c]='#';
            dfs(r,c,maxrow,maxcol);
        }
    }
    return ans;
}
int main()
{
    int tt,maxrow,maxcol,h,i,j;
    scanf("%d",&tt);
    for(int h=1;h<=tt;h++)
    {
        scanf("%d %d",&maxcol,&maxrow);
        ans=1;
        for(int r=1;r<=maxrow;r++)
        for(int c=1;c<=maxcol;c++)
        {
            scanf(" %c",&grid[r][c]);
            if(grid[r][c]=='@')
            {
                i=r; j=c;
                grid[r][c]='#';
            }
        }
        printf("Case %d: %d\n",h,dfs(i,j,maxrow,maxcol));

    }
    return 0;
}
