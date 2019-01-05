#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

const int mr[]= {0,-1,-1,-1,0,1,1,1,0};
const int mc[]= {1,1,0,-1,-1,-1,0,1,0};

bool flag=false;

string name;

struct data
{
    int row,col;
};
data tmp;

vector<data>pos[30];

int mxrow,mxcol;
bool Flag[31][31][16];
char arr[32][32];

string move(int index)
{
    if(index==0) return "R";
    if(index==1) return "UR";
    if(index==2) return "U";
    if(index==3) return "UL";
    if(index==4) return "L";
    if(index==5) return "DL";
    if(index==6) return "D";
    if(index==7) return "DR";
    if(index==8) return "*";
}

bool check(int row,int col)
{
    if(row>=0 && row<mxrow && col>=0 && col<mxcol) return true;
    else return false;
}

vector<string> dfs(int rr,int cc,int pos,vector<string>vec)
{
    Flag[rr][cc][pos]=true;
    if(pos==name.size())
    {
        flag=true;
        return vec;
    }
    if(flag==true) return vec;

    vector<string>ans,use;
    ans.push_back("-1");

    for(int i=0; i<9; i++)
    {
        int row=rr+mr[i];
        int col=cc+mc[i];

        if(check(row,col))
        {
            if(arr[row][col]==name[pos])
            {
                use=vec;
                use.push_back(move(i));
                if(flag==false && Flag[row][col][pos+1]==false)
                    ans=dfs(row,col,pos+1,use);
            }
        }
    }
    return ans;

}

int main()
{
    int tc;
    scanf(" %d",&tc);

    for(int tt=1; tt<=tc; tt++)
    {
        for(int i=0;i<=27;i++) pos[i].clear();

        scanf(" %d %d",&mxrow,&mxcol);

        for(int i=0; i<mxrow; i++)
        {
            for(int j=0; j<mxcol; j++)
            {
                scanf(" %c",&arr[i][j]);
                tmp.col=j;
                tmp.row=i;

                pos[arr[i][j]-'A'].push_back(tmp);
            }
        }

        int N;
        scanf(" %d",&N);

        printf("Case %d:\n",tt);

        for(int nn=0; nn<N; nn++)
        {
            cin>>name;
            bool name_found=false;
            int index=name[0]-'A';
            memset(Flag,false,sizeof Flag);
            for(int it=0; it<pos[index].size(); it++)
            {
                if(name_found) break;
                flag=false;
                vector<string> ans;
                ans.clear();

                ans=dfs(pos[index][it].row,pos[index][it].col,1,ans);

                if(ans[0]=="-1") continue;
                else
                {
                    name_found=true;
                    cout<<name<<" found:";
                    printf(" (%d,%d)",pos[index][it].row+1,pos[index][it].col+1);

                    for(int i=0;i<ans.size();i++) cout<<", "<<ans[i];
                    cout<<endl;
                }

            }

            if(name_found==false) cout<<name<<" not found"<<endl;

        }
    }
    return 0;
}
