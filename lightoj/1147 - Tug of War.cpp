#pragma comment(linker, "/STACK:60000000")

#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>

#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <iomanip>
#include <ctime>
#include <assert.h>

using namespace std;

//Type Definition
typedef long long ll;

#define REP(i,n) for (i=0;i<n;i++)
#define Clear(x,with) memset(x,with,sizeof(x))
#define SZ(x) (int)x.size()
#define pb push_back
#define popcount(i) __builtin_popcount(i)
#define gcd(a,b)    __gcd(a,b)
#define lcm(a,b) ((a)*((b)/gcd(a,b)))
#define two(X) (1<<(X))
#define twoL(X) (((ll)(1))<<(X))
#define setBit(mask,i) (mask|two(i))
#define contain(S,X) (((S)&twoL(X))!=0)

#define INF (1<<28)
#define SIZE 110000

ll dp[SIZE];
int arr[SIZE];

int main()
{
    int i,j,test,Case=1,x,y,p,q,N,sum,diff,minv;

    scanf("%d",&test);

    while(test--)
    {
        scanf("%d",&N);
        sum=0;
        REP(i,N)
        {
            scanf("%d",&arr[i]);
            sum+=arr[i];
        }
        //REP(i,sum+1) dp[i]=0;
        Clear(dp,0);
        dp[0]=two(0);
        REP(i,N)
        {
            for(j=sum-arr[i];j>=0;j--)
            {
                if(dp[j])
                    dp[j+arr[i]]=dp[j+arr[i]] | (dp[j]<<1);
            }
        }

        p=N/2;
        q=(N+1)/2;
        minv=INF;
        REP(i,sum+1)
            if(contain(dp[i],p) || contain(dp[i],q))
            {
                diff=abs((sum-i) - i);
                if(diff<minv)
                {
                    minv=diff;
                    x=min(i,sum-i);
                    y=max(i,sum-i);
                }
            }
        printf("Case %d: %d %d\n",Case++,x,y);
    }

    return 0;
}
