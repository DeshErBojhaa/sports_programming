#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

#define SN 40000
#define HP 200

double dpv[SN+1][HP+1], dpe[SN+1][HP+1];
int hp[2], dt[2], l[2], r[2], p[2];
double eps = 1e-8;

int main()
{
    printf("%d  %d  %d\n\n\n\n",6^1,5^2,4^3);
    int i, j, k;
    for (i=0; i<2; i++) cin>>hp[i]>>dt[i]>>l[i]>>r[i]>>p[i];
    dpv[0][hp[0]] = 1, dpe[0][hp[1]] = 1;

    double x1 = p[1]*0.01;   /// making probability decimal
    double x0 = p[0]*0.01;   /// making probability decimal
    double c1 = (1-x1)/(r[1]-l[1]+1);  /// expected value of heat
    double c0 = (1-x0)/(r[0]-l[0]+1);  /// expected value of heat

    int l0=l[0],l1=l[1],r1=r[1],r0=r[0];
    bool flag=0;

    for (i=0; i<SN; i++)
    {
        dpv[i+1][0] = dpv[i][0];
        for (j=1; j<=hp[0]; j++)
        {
            if (dpv[i][j]<eps) continue;
            flag = 1;
            dpv[i+1][j] += dpv[i][j]*x1;  /// missing the shot
            double tmp = dpv[i][j]*c1;    /// hitting the shot
            for (k=l1; k<=r1; k++)
            {
                dpv[i+1][max(0,j-k)] += tmp;
            }
        }
        if (!flag) break;
    }

    flag = 0;

    for (i=0; i<SN; i++)
    {
        dpe[i+1][0] = 0;
        for (j=1; j<=hp[1]; j++)
        {
            if (dpe[i][j]<eps) continue;
            flag = 1;
            dpe[i+1][j] += dpe[i][j]*x0;
            double tmp = dpe[i][j]*c0;
            for (k=l0; k<=r0; k++)
            {
                dpe[i+1][max(0,j-k)] += tmp;
            }
        }
        if (!flag) break;
    }

    double ans = 0;
    for (i=1; i<=SN; i++)   /// shot number
    {
        int t = ((i-1)*dt[0]+dt[1]-1)/dt[1];
        ans += (1-(t>SN?0:dpv[t][0]))*(dpe[i][0]);//
    }

    cout<<ans<<endl;
}
