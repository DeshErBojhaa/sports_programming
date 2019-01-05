#include<stdio.h>
#include<queue>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

struct data
{
    int row,col,cost;
};

vector<data>vec1,vec2,use;

const int mr[]= {-1,0,1,0};
const int mc[]= {0,1,0,-1};
const int inf=1<<28;

int rlim,clim,dys[202][202],erow,ecol,srow,scol;
char fild[202][202];

int bfs()
{
    memset(dys,0,sizeof dys);

    queue<int>Q;
    Q.push(srow);
    Q.push(scol);

    while(Q.size())
    {
        int brow=Q.front();
        Q.pop();
        int bcol=Q.front();
        Q.pop();

        for(int i=0; i<4; i++)
        {
            int nrow=brow+mr[i];
            int ncol=bcol+mc[i];

            if(dys[nrow][ncol]==0 && ( (fild[nrow][ncol]=='.') || (fild[nrow][ncol]=='D') || (fild[nrow][ncol]=='*') ) )
            {
                if((fild[nrow][ncol]=='*')) dys[nrow][ncol]=dys[brow][bcol]+3;
                else
                dys[nrow][ncol]=dys[brow][bcol]+1;

                Q.push(nrow);
                Q.push(ncol);
            }
        }
    }
    return dys[erow][ecol];
}

void system(int brow,int bcol)
{
    memset(dys,0,sizeof dys);
    use.clear();

    queue<int>Q;
    Q.push(brow);
    Q.push(bcol);

    while(Q.size())
    {
        int bsrow=Q.front();
        Q.pop();
        int bscol=Q.front();
        Q.pop();

        for(int i=0; i<4; i++)
        {
            int nrow=bsrow+mr[i];
            int ncol=bscol+mc[i];

            if(dys[nrow][ncol]==0 && fild[nrow][ncol]!='#')
            {
                dys[nrow][ncol]=dys[bsrow][bscol]+1;

                if(fild[nrow][ncol]=='.')
                {
                    Q.push(nrow);
                    Q.push(ncol);
                }

                if(fild[nrow][ncol]=='*')
                {
                    data tmp;
                    tmp.row=nrow;
                    tmp.col=ncol;
                    tmp.cost=dys[nrow][ncol];

                    use.push_back(tmp);
                }
            }
        }
    }
    return;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        vec1.clear();
        vec2.clear();
        use.clear();

        int tara=0;
        scanf(" %d %d",&rlim,&clim);

        for(int i=0; i<rlim; i++)
            for(int j=0; j<clim; j++)
            {
                scanf(" %c",&fild[i][j]);
                if(fild[i][j]=='*') tara++;
                if(fild[i][j]=='P')
                {
                    srow=i;
                    scol=j;
                }
                if(fild[i][j]=='D')
                {
                    erow=i;
                    ecol=j;
                }
            }

        if (tara<=1)
        {
            for(int i=0; i<rlim; i++)
                for(int j=0; j<clim; j++)
                    if(fild[i][j]=='*') fild[i][j]='#';
        }

            int ans1= bfs();

            if(ans1==0) ans1=inf;
            int ans2=inf;

            system(srow,scol);
            vec1=use;
            system(erow,ecol);
            vec2=use;

            for(int i=0; i<vec1.size(); i++)
                for(int j=0; j<vec2.size(); j++)
                {
                    if(  (vec1[i].row == vec2[j].row) && (vec1[i].col== vec2[j].col)  )continue;
                    ans2=min(ans2,(vec1[i].cost+vec2[j].cost+1));
                }

            if(min(ans1,ans2)>=inf)  printf("Case %d: impossible\n",tt);
            else printf("Case %d: %d\n",tt,min(ans1,ans2));

    }
    return 0;

}

/*
8
6 8
########
#P.....#
#*.....#
#......#
#D.....#
########
5 10
##########
#...#....#
#...#....#
#.*P#D.*.#
##########
11 10
##########
#*#.....D#
###.###.##
#...#.#..#
#.....##.#
#####*####
#........#
#........#
#........#
#P.......#
##########
4 10
##########
#.P..#*..#
#*......D#
##########
3 9
#########
#P.#..D.#
#########
5 7
#######
#..#..#
#*P*D.#
#..#..#
#######
5 9
#########
#*......#
#P.....D#
#......*#
#########
3 14
##############
#*..P*D.....*#
##############

*/
