#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

int main()
{
    int T,arr[51][51],final[51];
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        memset(final ,0,sizeof final);
        int row,col;
        scanf(" %d %d",&row,&col);

        for(int i=0;i<row;i++)
           for(int j=0;j<col;j++)
           {
               scanf(" %d",&arr[i][j]);
               final[i]+=arr[i][j];
           }

        int ans=final[0];
        for(int i=1;i<row;i++) ans=ans^final[i];
        if(ans==0) printf("Case %d: Bob\n",t);
        else
        printf("Case %d: Alice\n",t);
    }
    return 0;
}
