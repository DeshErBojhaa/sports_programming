#include<stdio.h>
#include<map>

using namespace std;

char mat[101][101];
map<char,int>mp;

int main()
{
    int row,col;
    scanf(" %d %d",&row,&col);

    for(int i=0;i<row;i++)
        for(int j=0;j<col;j++)
            scanf(" %c",&mat[i][j]);

    long long ans=1;

    for(int i=0;i<col;i++)
    {
        int ind=2;
        mp.clear();

        for(int j=0;j<row;j++)
        {
            if(mp[mat[j][i]]==0) mp[mat[j][i]]=++ind;
        }

        ans*=mp.size();
        ans%=1000000007;
    }

    printf("%d\n",ans);
    return 0;
}
