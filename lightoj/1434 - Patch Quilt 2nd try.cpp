#include<stdio.h>
#include<algorithm>
#include<string>
#include<string.h>
#include<queue>
#include<vector>
#include<iostream>

using namespace std;

const int mr[]= {0,-1,-1,-1,0,1,1,1};
const int mc[]= {1,1,0,-1,-1,-1,0,1};

struct cord
{
    int row,col;
};
cord tmp;

vector<cord>beg[30];
vector<string>path;

int mxrow,mxcol;
int flag[33][33];

char arr[33][33];
string name;

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
}

bool chk(int row,int col,int ind)
{
    if(row>=0 && row<mxrow && col>=0 && col<mxcol && ind<name.size()) return true;
    else return false;
}

bool bfs(int sr,int sc)
{
    memset(flag,0,sizeof flag);
    int index=1;
    queue<int>Q;
    Q.push(sr);
    Q.push(sc);

    while(Q.size())
    {
        int currow=Q.front();
        Q.pop();
        int curcol=Q.front();
        Q.pop();

        if(arr[currow][curcol]==name[index])
        {
            Q.push(currow);
            Q.push(curcol);
            flag[currow][curcol]=index;
            index++;
        }
        else
            for(int i=0; i<8; i++)
            {
                int nerow=currow+mr[i];
                int necol=curcol+mc[i];

                if(chk(nerow,necol,index)==true)
                {
                    if(arr[nerow][necol]==name[index])
                    {
                        Q.push(nerow);
                        Q.push(necol);
                        flag[nerow][necol]=index;
                        index++;
                    }
                }
            }
    }
    if(index==name.size()) return true;
    else return false;
}

void find_path(int rr,int cc)
{
    int curval=flag[rr][cc];
    int nextval=1<<30;

    while(flag[rr][cc])
    {
        path.push_back("*");
        flag[rr][cc]--;
    }

    queue<int>Q;
    Q.push(rr);
    Q.push(cc);
int ball=0;
    while(Q.size())
    {
        ball++;
        if(ball==6) break;
        cout<<"BALL "<<ball<<endl;

        int nextval=1<<30,sendind=0;
        int baserow=Q.front();
        Q.pop();
        int basecol=Q.front();
        Q.pop();

        for(int i=0; i<8; i++)
        {
            int nrow=baserow+mr[i];
            int ncol=basecol+mc[i];

            if(flag[nrow][ncol]<nextval && flag[nrow][ncol]>curval)
            {
                nextval=flag[nrow][ncol];
                printf("Curval %d Next val %d\n",curval,nextval);
                sendind=i;
            }
        }

        for(int pp=curval; pp<=(nextval-curval-1); pp++) path.push_back("*");

        if(nextval>curval)
        {
            Q.push(baserow+mr[sendind]);
            Q.push(basecol+mc[sendind]);
            path.push_back(move(sendind));
            curval=nextval;
        }

    }

    return;
}

int main()
{
    int T,N;

    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        for(int i=0; i<30; i++) beg[i].clear();

        scanf(" %d %d",&mxrow,&mxcol);

        for(int i=0; i<mxrow; i++)
        {
            for(int j=0; j<mxcol; j++)
            {
                scanf(" %c",&arr[i][j]);
                tmp.row=i;
                tmp.col=j;

                beg[arr[i][j]-'A'].push_back(tmp);
            }
        }
        scanf(" %d",&N);
        printf("Case %d:\n",tt);

        for(int x=0; x<N; x++)   /// Taking a name
        {
            cin>>name;

            bool gotnam=false;


            for(int i=0; i<beg[name[0]-'A'].size(); i++)
                if(gotnam==false)
                {
                    int rr=beg[name[0]-'A'][i].row;
                    int cc=beg[name[0]-'A'][i].col;

                    bool ase=bfs(rr,cc);
                    if(ase==false) continue;
                    else
                    {
                        cout<<name<<" found: ";
                        printf(" (%d,%d)",rr+1,cc+1);
                        gotnam=true;

                        path.clear();

                        cout<<endl;
                        for(int xx=0; xx<4; xx++)
                        {
                            for(int yy=0; yy<4; yy++) printf("%d",flag[xx][yy]);
                            printf("\n");
                        }
                        find_path(rr,cc);

                        for(int ind=0; ind<path.size(); ind++)
                            cout<<", "<<path[i];
                        printf("\n");
                    }
                }

            if(gotnam==false) cout<<name<<" not found"<<endl;


        }

    }
    return 0;
}

/*

1
4 4
qwer
tyui
asdf
ghjk
1

*/

