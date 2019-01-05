#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<map>

using namespace std;

int vec[55][55];

int nob,dp[50][50][50];

vector< pair<int,int> >fvec;


int rec(int cur,int left,int right)
{
    printf("CUR %d  LEFT %d  RIGHT %d\n",cur,left,right);
    if(left==right) return 1;
    if(left>right) return 0;

    int &ret=dp[cur][left][right];
    if(ret!=-1) return ret;
    ret=0;

    int pivot,sl,sr,index=0;

    bool flag[1000];
    memset(flag,false,sizeof flag);

    for(int i=left; i<=right; i++)
    {
        pivot=vec[cur][i];

        sl=left-1;
//        index=0;

        for(int j=left; j<=right; j++)
        {
            if(vec[cur][j]>=pivot)
            {
                if(j-sl >=2 )
                {
                    index ^= rec(cur,sl+1,j-1);
                }
                sl = j;
            }

        }

        if((right+1)-sl >=2)
        {
            index ^= rec(cur , sl+1,right);
        }

        flag[index]=true;
    }

    int i;
    for(i=0; i<1001; i++)
        if(flag[i]==false) break;

    ret=i;

    return ret;
}

int main()
{
    int tc,nop[55];
    scanf(" %d",&tc);

    for(int tt=1; tt<=tc; tt++)
    {
        scanf(" %d",&nob);

        for(int i=0; i<nob; i++)
        {
            int tmp;

            scanf(" %d",&nop[i]);
            for(int j=0; j<nop[i]; j++)
            {
                scanf(" %d",&vec[i][j]);
            }
        }

        memset(dp,-1,sizeof dp);
        int ans=0;
        for(int i=0; i<nob; i++)
            ans=ans^rec(i,0,nop[i]-1);

        printf("Case %d:",tt);
        if(ans)
        {
            cout<<"ANS "<<ans<<endl;
            printf(" Aladdin\n");
            fvec.clear();

            for(int i=0; i<nob; i++)   /// bracelet choose  i
            {
                map<int , int > mp;
                mp.clear();

                int ball=0;
                ball^=rec(i,0,nop[i]-1);

                for(int j=0; j<nop[i]; j++)   /// particular point choose
                {
                    int pivot=vec[i][j],sl=-1,sr;

                    for(int k=0; k<nop[i]; k++)
                    {
                        if(vec[i][k]<pivot && sl==-1)
                            sl=k;

                        if(vec[i][k]>=pivot && sl!=-1)
                        {
                            sr=k-1;
                            ball^=rec(i,sl,sr);
                            sl=-1;
                        }
                    }

                    if(sl!=-1) ball^=rec(i,sl,nop[i]-1);

                    ball=ball^ans;

                    if(ball==0)
                    {
                        if(mp[vec[i][j]]==0)
                        {
                            fvec.push_back(make_pair(i+1,vec[i][j]));
                            mp[vec[i][j]]=10+i;
                        }
                    }

                }
//                for(int ii=0; ii<fvec.size(); ii++ ) printf("(%d %d) ",fvec[ii].first,fvec[ii].second);
//                cout<<"  end "<<endl;
            }
            for(int ii=0; ii<fvec.size(); ii++ ) printf("(%d %d) ",fvec[ii].first,fvec[ii].second);
            printf("\n");


        }
        else printf(" Genie\n");

    }
    return 0;
}
