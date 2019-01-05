#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

int cs,T,ROW,COL,dp[102][6565],three[10];
char arr[102][10],tmp[102][10];

int rec(int row,int mask);
int Generate(int row,int col,int mask,int cur)
{
    if(col==COL)   /// chk this case
    {
        int send_mask=0;
        for(int i=0;i<col;i++)
        {
            if( ((mask/three[i])%3)==2 && (cur&(1<<i)) ) send_mask+=2*three[i];
            else if( (((mask/three[i])%3)==2) && ((cur&(1<<i))==0) ) send_mask+=three[i];
        }
        return rec(row+1,send_mask);
    }
    int bit1=(mask/three[col])%3;
    int bit2=(mask/three[col+1])%3;
    int bit3=(mask/three[col+2])%3;

    if(row-2>=0 && col+2<COL)
    {
        if(bit1==0 && bit2==0 && bit3==0 && arr[row-2][col]=='.' && arr[row-2][col+1]=='.' && arr[row-2][col+2]=='.')
    }

}

int rec(int row,int mask)
{
    if(row==ROW)
    {
        if(!mask) return 1;
        return 0;
    }
    int &ret=dp[row][mask];
    if(ret!=-1) return ret;
    ret=0;

    ret+=Generate(row,0,mask,0);

    return ret;
}

int main()
{
    three[0]=1;
    for(int i=1;i<10;i++) three[i]=three[i-1]*3;
    scanf(" %d",&T);
    for(cs=1;cs<=T;cs++)
    {
        scanf(" %d %d",&ROW,&COL);
        for(int i=0;i<ROW;i++)
            for(int j=0;j<COL;j++) scanf(" %c",&arr[i][j]);

        if(ROW<COL)
        {
            for(int i=ROW-1,l=0; i>=0; i--,l++)
                for(int j=0,k=0; j<COL; j++,k++)
                    tmp[k][l]=arr[i][j];
            swap(ROW,COL);
            for(int i=0;i<ROW;i++) for(int j=0;j<COL;j++) arr[i][j]=tmp[i][j];

        }
        memset(dp,-1,sizeof dp);
        printf("Case %d: %d\n",tt,rec(0,0));
    }
    return 0;
}
