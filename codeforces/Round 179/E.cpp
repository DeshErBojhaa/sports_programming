#include<stdio.h>
#include<algorithm>
#include<vector>
#include<set>
#include<iostream>

using namespace std;

const int mod=1000000007;
const int inf=(int) 1<<29;

int sm,bg,n,boat,NcR[51][51],dp[51][51][2],pd[51][51][2],tmp;

struct data
{
    int small,big,side,move;
    data(int small,int big,int side,int move) : small(small) , big(big) , side(side), move(move) {}
};

bool operator<(data a, data b)
{
    if(a.move==b.move)
    {
        if(a.small==b.small)
        {
            if(a.big==b.big)
            {
                return a.side<b.side;
            }
            else return a.big<b.big;
        }
        else return a.small<b.small;
    }
    else return a.move<b.move;
}


//bool operator<(data a, data b)
//{
//    return a.move < b.move || a.move == b.move && ( a.small < b.small || a.small == b.small && (a.big < b.big || a.big == b.big && a.side < b.side) );
//}


set<data>ss;

void comb()
{
    for(int i=0;i<51;i++)
    NcR[i][0]=1;

    for(int i=1;i<51;i++)
        for(int j=1;j<=i;j++)
            NcR[i][j]=(NcR[i-1][j-1]+NcR[i-1][j])%mod;

    return;
}

inline int func(int sofar, int r1,int n1 ,int r2,int n2)
{
    return int ((1ll * sofar * (1ll * (NcR[n1][r1]) * (NcR[n2][r2]))%mod )%mod);
}

int main()
{
    comb();

    cin>>n>>boat;
    boat/=50;

    for(int i=0;i<n;i++)
    {
        scanf(" %d",&tmp);
        tmp/=50;

        if(tmp==1) sm++;
        else bg++;
    }

    for(int i=0;i<51;i++)
       for(int j=0;j<51;j++)
           for(int k=0;k<2;k++) dp[i][j][k]=inf;

     pd[0][0][0]=1;
     dp[0][0][0]=0;

    ss.insert(data(0,0,0,0));

    while(ss.size())
    {
        int small=ss.begin()->small;
        int big=ss.begin()->big;
        int side=ss.begin()->side;
        int move=ss.begin()->move;
        int total=pd[small][big][side];

//        cout<<small<<"  "<<big<<"  "<<side<<"  "<<move<<"  "<<total<<endl;
        ss.erase(ss.begin());

        if(side==0)
        {
            for(int i=0;i<=boat && i+small <=sm; i++)
                for(int j=0; i+(j*2)<=boat && j+big <=bg ;j++)
                    if(i+j>0)
                    {
                        if(dp[i+small][j+big][1-side] >= move+1)
                        {
                            if(dp[i+small][j+big][1-side] > move+1)
                            {
                                ss.erase(data (i+small , j+big , 1-side , dp[i+small][j+big][1-side]));
                                dp[i+small][j+big][1-side] = move+1;
                                pd[i+small][j+big][1-side] = func(total, i, sm-small, j, bg-big);
//                                cout<<total<<" "<<i<<" "<<sm-small<<" "<<j<<" "<<bg-big<<endl;
//                                cout<<">> "<<func(total, i, sm-small, j, bg-big)<<endl;
                                ss.insert(data (i+small , j+big , 1-side , dp[i+small][j+big][1-side]));

                            }
                            else
                            {
                                pd[i+small][j+big][1-side] += func(total, i, sm-small, j, bg-big);
                                pd[i+small][j+big][1-side] %=mod;
                            }
                        }
                    }
        }
        else
        {
            for(int i=0;i<=small && i<=boat ;i++)
                for(int j=0;j<=big && i+(j*2)<=boat; j++)
                if(i+j>0)
                {
                    if(dp[small-i][big-j][1-side] >= move+1)
                    {
                        if(dp[small-i][big-j][1-side] > move+1)
                        {
                            ss.erase(data (small-i, big-j , 1-side , dp[small-i][big-j][1-side] ) );
                            dp[small-i][big-j][1-side] = move+1;
                            pd[small-i][big-j][1-side] = func(total, i, small, j, big);
                            ss.insert(data (small-i, big-j , 1-side , dp[small-i][big-j][1-side] ));
                        }
                        else
                        {
                            pd[small-i][big-j][1-side] += func(total, i, small, j, big);
                            pd[small-i][big-j][1-side] %= mod;
                        }
                    }
                }
        }


    }

    if(dp[sm][bg][1]==inf) printf("-1\n0\n");
    else
    printf("%d\n%d\n",dp[sm][bg][1],pd[sm][bg][1]);

    return 0;
}
