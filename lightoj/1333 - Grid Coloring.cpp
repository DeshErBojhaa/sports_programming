/// Stuck IN it  any help (testcase or idea) will be a great hand  (:

#include<stdio.h>
#include<algorithm>
#include<iostream>

using namespace std;

typedef long long ll;

struct data
{
    ll rr,cc;
};
data Blocked_Cell[505];  /// An array contains only row and columns of blocked cells
data tmp;

const ll mod=1000000000;   /// as statement says 10^9

ll row,col,TYPE,B;

/// TYPE = Number of Colors
/// B    = Number of Blocked Cells

bool com(data a,data b)
{
    if(a.cc==b.cc) return a.rr<b.rr;
    else return a.cc<b.cc;
}

ll make_pow(ll base, ll to_pow)
{
    if(base==0) return 0;       /// Not needed used for a fast runtime
    if(base == 1) return (ll)1; /// Not needed used for a fast runtime

    if(to_pow==1)     return base;
    if(to_pow==0) return (ll)1;

    ll ret=make_pow(base,to_pow/2);
    ret%=mod;
    ret=(ret*ret)%mod;

    if(to_pow%2) ret=(ret*base)%mod;

    return ret%mod;
}

int main()
{
    int T;
    ll a,b;

    scanf(" %d",&T);

    for(int tt=1; tt<=T; tt++)
    {
        scanf(" %lld %lld %lld %lld",&row,&col,&TYPE,&B);

        ll ans=1;

        for(ll i=0; i<B; i++)
        {
            scanf(" %lld %lld",&a,&b);
            tmp.rr=a;
            tmp.cc=b;

            Blocked_Cell[i]=tmp;
        }

        sort(Blocked_Cell,Blocked_Cell+B,com); /// Sorting according to Column first then Row

        ll reduce=0;


        for(int i=0; i<B; i++)
        {

            int Now_Row=Blocked_Cell[i].rr;
            int Now_Col=Blocked_Cell[i].cc;

            if(Now_Row == 1 || Now_Row== row)     reduce++;  ///Chk weather block at top or at bottom
            if(Now_Row == 1 && Now_Row== row)     reduce++;

            for(int j=i+1;j<B;j++)
            {
                if(Blocked_Cell[j].cc != Now_Col  ) break;   /// break if j represents another column than Now_col
                if( (abs(Blocked_Cell[j].rr-Now_Row)>1) ) break;

                if(Blocked_Cell[j].cc == Now_Col)
                {
                    if(Now_Row+1 == Blocked_Cell[j].rr) reduce++; /// Chk if two blocks are consecutive // cout<<"CONSEC "<<endl;
                }
            }

        }


        ll Num_Typ1=(col-reduce+B);

        ll Num_Typ2=((row*col)-(Num_Typ1+B));

        ans*=make_pow(TYPE,Num_Typ1);
        ans%=mod;

        if(Num_Typ2>0)
            ans*=make_pow(TYPE-1,Num_Typ2);
        ans%=mod;

        printf("Case %d: %lld\n",tt,ans);
    }
    return 0;
}

/*
111
4 6 2 11
1 1
1 4
1 6
2 3
2 6
3 2
3 6
4 1
4 3
4 5
4 6
2 2 5 4
1 1
1 2
2 1
2 2
8 1 3 4
1 1
3 1
5 1
8 1
7 2 3 8
2 1
3 1
4 1
5 1
1 2
2 2
6 2
7 2
3 4 3 4
1 1
1 2
1 3
1 4
4 3 3 4
1 1
2 1
3 1
4 1
3 4 3 4
2 1
2 2
2 3
2 4

*/
