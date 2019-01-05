#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>


using namespace std;

vector<int>vec[55];
vector<pair<int,int> >V;
int nob,nop,tmp_int,dp[51][51][51];

int rec(int cur,int lf,int rt)
{
    if(lf==rt) return 1;

    int &ret=dp[cur][lf][rt];
    if(ret!=-1) return ret;

    int Left=-1,Right=-1,ind=0;

    bool lag[59];
    memset(lag,false,sizeof lag);

    for(int i=lf; i<=rt; i++)
    {
        int pvt=vec[cur][i];
        ind=0;
        Left=-1;
        Right=-1;
        for(int j=lf; j<=rt; j++)
        {
            if(vec[cur][j]<pvt)
            {
                if(Left==-1) Left=j;
                else Right=j;
            }
            else
            {
                if(Left!=-1 && Right!=-1) ind^=rec(cur,Left,Right);
                if(Left!=-1 && Right==-1) ind^=1;

                Left=-1;
                Right=-1;
            }
        }
        if(Left!=-1 && Right!=-1 ) ind^=rec(cur,Left,Right);
        if(Left !=-1 && Right==-1) ind^=1;

        lag[ind] = true;
    }

    int tx=0;
    for(tx=0;; tx++)
    {
        if(lag[tx]==false)
        {
            ret=tx;
            break;
        }
    }

    return ret;
}


int main()
{
    int T;
    scanf(" %d",&T);
    for(int tt=1; tt<=T; tt++)
    {
        int ans=0;
        scanf(" %d",&nob);

        memset(dp,-1,sizeof dp);

        for(int i=0; i<nob; i++)
        {
            vec[i].clear();
            scanf(" %d",&nop);
            for(int j=0; j<nop; j++)
            {
                scanf(" %d",&tmp_int);
                vec[i].push_back(tmp_int);
            }
            ans^=rec(i,0,(int)(vec[i].size()-1));
        }

        printf("Case %d: ",tt);
        if(ans==0) printf("Genie\n");
        else
        {
            V.clear();
            printf("Aladdin\n");
            for(int i=0; i<nob; i++)
            {
                int maal=ans^rec(i,0,(int)(vec[i].size()-1));
                int baal=0;

                bool flag[100009];
                memset(flag,false,sizeof flag);

                int left=-1,right=-1;

                for(int j=0; j<vec[i].size(); j++)
                {
                    baal=0;
                    left=-1;
                    right=-1;
                    int pivot=vec[i][j];

                    for(int k=0; k<vec[i].size(); k++)
                    {
                        if(vec[i][k]<pivot)
                        {
                            if(left==-1) left=k;
                            else right=k;
                        }
                        else
                        {
                            if(left!=-1 && right!=-1) baal^=rec(i,left,right);
                            if(left!=-1 && right==-1) baal^=1;

                            left=-1;
                            right=-1;
                        }
                    }

                    if(left!=-1 && right!=-1 ) baal^=rec(i,left,right);
                    if(left !=-1 && right==-1) baal^=1;

                    if((baal^maal)==0)
                    {
                        if(flag[pivot]==false)
                        {
                            flag[pivot]=true;
                            V.push_back(make_pair(i+1,pivot));
                        }
                    }

                }
            }

            sort(V.begin(),V.end());

            for(int i=0; i<V.size(); i++)
                printf("(%d %d)",V[i].first,V[i].second);
            printf("\n");
        }



    }
    return 0;
}
