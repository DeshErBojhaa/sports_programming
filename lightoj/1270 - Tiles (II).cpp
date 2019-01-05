#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

typedef unsigned long long ull;

int cs,T,ROW,COL;
char arr[102][102],tmp[102][102];
ull dp[102][1<<8];
bool flag[102][1<<8];

bool chk(int mask,int i)
{
    if((mask&(1<<i))==0) return false;
    return true;
}

bool arrok(int row,int col)
{
    if(arr[row][col]=='.') return true;
    else return false;
}

ull process(int row,int col,int prev,int cur);
ull rec(int row,int mask)
{
    if(row==ROW) return (mask==0);
    ull &ret=dp[row][mask];
    if(flag[row][mask]) return ret;
    ret=0;
    flag[row][mask]=true;

    ret+=process(row,0,mask,0);

    return ret;
}

ull process(int row,int col,int prev,int cur)
{
    ull ret=0;
    if(col==COL) return rec(row+1,cur);

    if(arr[row][col]=='.' && chk(prev,col)==false)
    {
        if(row+1<ROW && arrok(row+1,col) && chk(cur,col)==false)
            ret+=process(row,col+1,prev,cur|(1<<col));

        if(col+1<COL && arrok(row,col+1) && chk(prev,col+1)==false)
            ret+=process(row,col+2,prev,cur);

        if(row+1<ROW && col+1<COL && chk(cur,col)==false && chk(cur,col+1)==false && arrok(row+1,col) && arrok(row+1,col+1))
            ret+=process(row,col+1,prev,cur|(1<<col)|(1<<(col+1)));

        if(row+1<ROW && col+1<COL && arrok(row,col+1) && arrok(row+1,col) && chk(prev,col+1)==false && chk(cur,col)==false)
            ret+=process(row,col+2,prev,cur|(1<<col));

        if(row+1<ROW && col-1>=0 && chk(cur,col-1)==false && chk(cur,col)==false && arrok(row+1,col-1) && arrok(row+1,col))
            ret+=process(row,col+1,prev,cur|(1<<col)|(1<<(col-1)));

        if(row+1<ROW && col+1<COL && arrok(row,col+1) && arrok(row+1,col+1) && chk(prev,col+1)==false && chk(cur,col+1)==false)
            ret+=process(row,col+2,prev,cur|(1<<(col+1)));
    }
    else
        ret+=process(row,col+1,prev,cur);

        return ret;
}

int main()
{
    scanf(" %d",&T);
    for(cs=1;cs<=T;cs++)
    {
        scanf(" %d %d",&ROW,&COL);
        for(int i=0;i<ROW;i++)
            for(int j=0;j<COL;j++) scanf(" %c",&arr[i][j]);

        if(COL>ROW)
        {
            for(int i=ROW-1,l=0; i>=0; i--,l++)
                for(int j=0,k=0; j<COL; j++,k++)
                    tmp[k][l]=arr[i][j];

            swap(ROW,COL);
            for(int i=0; i<ROW; i++)
            {
                for(int j=0; j<COL; j++)
                {
                    arr[i][j]=tmp[i][j];
                }
            }
        }

        memset(flag,false,sizeof flag);
        ull ans=rec(0,0);
        printf("Case %d: ",cs);
        cout<<ans<<endl;
    }
    return 0;
}

