#include<algorithm>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<queue>

using namespace std;

int n,manp[105][105],womp[105][105],enged_with[105],relation[105][105];


int find_index(int ind,int target,int n)
{
    for(int i=0;i<n;i++) if(womp[ind][i]==target) return i;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        queue<int>q;
        memset(relation,0,sizeof relation);
        memset(enged_with,-1,sizeof enged_with);

        scanf(" %d",&n);
        for(int i=0;i<n;i++) q.push(i);

        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                scanf(" %d",&manp[i][j]);
                manp[i][j]-=n+1;
            }
        }

        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
            {
                scanf(" %d",&womp[i][j]);
                womp[i][j]--;
            }



        while(q.size())
        {
            int jamai=q.front();
            q.pop();

            for(int i=0; i<n; i++)      /// select bou
            {
                int bou=manp[jamai][i];

                if(relation[jamai][bou]==0)
                {
                    relation[jamai][bou]=1;

                    if(enged_with[bou]==-1)     /// brand new bou
                    {
                        enged_with[bou]=jamai;
                        break;
                    }

                    else                        /// second hand
                    {
                        int old_jamai_indx= find_index(bou,enged_with[bou],n);
                        int new_jamai_indx= find_index(bou,jamai,n);

//                           int old_jamai_indx= indexing[bou][enged_with[bou]];
//                           int new_jamai_indx= indexing[bou][jamai];

                        if(new_jamai_indx<old_jamai_indx)
                        {
                            q.push(enged_with[bou]);
                            enged_with[bou]=jamai;
                            break;
                        }
                    }
                }
            }
        }
        printf("Case %d:",t);
        for(int i=0; i<n; i++) printf(" (%d %d)",enged_with[i]+1,i+n+1);
        printf("\n");
    }
    return 0;
}
