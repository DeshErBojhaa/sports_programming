#include<stdio.h>
#include<queue>
#include<vector>
#include<map>

using namespace std;

struct data
{
    int row,col;
};
queue<data>ForRow,ForCol;
vector<data>ans;
map<int,int>mp;

int main()
{
    int n;
    char hudai;
    scanf(" %d",&n);

    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
        {
            scanf(" %c",&hudai);
            if(hudai=='.')
            {
                data tmp;
                tmp.row=i;
                tmp.col=j;

                ForRow.push(tmp);
                ForCol.push(tmp);
            }
        }
    int index=1;
    while(ForRow.size())
    {
        data use=ForRow.front();
        ForRow.pop();

        if(mp[use.col]==0)
        {
            mp[use.col]=index++;
            ans.push_back(use);
        }
    }
    if((int)ans.size()==n)
    {
        for(int i=0; i<n; i++)
            printf("%d %d\n",ans[i].row+1,ans[i].col+1);
        return 0;
    }

    index=1;
    mp.clear();
    ans.clear();

    while(ForCol.size())
    {
        data use=ForCol.front();
        ForCol.pop();

        if(mp[use.row]==0)
        {
            mp[use.row]=index++;
            ans.push_back(use);
        }
    }
    if((int)ans.size()==n)
    {
        for(int i=0; i<n; i++)
            printf("%d %d\n",ans[i].row+1,ans[i].col+1);
        return 0;
    }
    printf("-1\n");
    return 0;
}
