/******************************
**     Solution by Zip753    **
**            78             **
******************************/

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <stack>
#include <utility>
#include <queue>
#include <deque>
#include <functional>
#include <list>

using namespace std;

#define WITH_FILES(A,B) {freopen(#A,"r",stdin);freopen(#B,"w",stdout);}
#define STD_FILES WITH_FILES(input.txt,output.txt)
#define INPUT(A) {freopen(#A,"r",stdin);}
#define OUTPUT(A) {freopen(#A,"w",stdout);}
#define forin(x,a) for (typeof((a).begin()) x=(a).begin(); x!=(a).end(); x++)
#define debug(x) cerr<< #x <<" = "<< (x) <<endl;
#define TESTS int tststs; scanf("%d", &tststs); while(tststs--)

#define pu push_back
#define po pop_back
#define mp make_pair
#define y1 stupid_cmath
#define y0 even_more_stupid_cmath
#define PI 3.14159265358979323848284338327950
template<class T> class priority_queue_min
{
public:
    typedef priority_queue<T,vector<T>,greater<typename vector<T>::value_type> > type;
};

typedef long long INT;
typedef long double ld;
typedef double dbl;
typedef vector<int> huge;
const INT INTINF=9223372036854775807ll;
const int INF=2147483647;
const int P=1000000007;
const int base=1000000000;
const dbl EPS = 1e-9;
const int dx[4]= {0,1,0,-1},dy[4]= {1,0,-1,0};

#if ( _WIN32 || __WIN32__ )
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

template<class T> inline T Max(T a, T b)
{
    return a > b ? a : b;
}

template<class T> inline T Min(T a, T b)
{
    return a < b ? a : b;
}

template<class T> inline T Abs(T a)
{
    return a > T(0) ? a : -a;
}

template<class T> inline T gcd(T a, T b)
{
    while (b>0)
    {
        a%=b;
        T c=a;
        a=b;
        b=c;
    };
    return a;
}

template<class T> inline void Swap(T &a, T &b)
{
    T c=a;
    a=b;
    b=c;
}

#define DEATH exit(0);
#define B_(x) ((x)-(((x)>>1)&0x77777777)-(((x)>>2)&0x33333333)-(((x)>>3)&0x11111111))
#define BITCOUNT(x) (((B_(x)+(B_(x)>>4)) & 0x0F0F0F0F) % 255)
#pragma comment(linker, "/STACK:67108864")

const int MAXN = 111;

struct T
{
    int x, y, fl, val;
    T (int x, int y, int fl, int val) : x(x), y(y), fl(fl), val(val) {}
};

bool operator<(T a, T b)
{
    return a.val < b.val || a.val == b.val && ( a.x < b.x || a.x == b.x && (a.y < b.y || a.y == b.y && a.fl < b.fl) );
}

int n, n1, n2;
int d[MAXN][MAXN][2];
int p[MAXN][MAXN][2];
int c[MAXN][MAXN];
int KK;

inline int f(int x, int k1, int n1, int k2, int n2)
{
    return int((1ll * x * ((1ll * c[n1][k1] * c[n2][k2]) % P)) % P);
}

int main()
{
    scanf("%d%d", &n, &KK);
    KK /= 50;
    if (KK == 0)
    {
        printf("-1\n0\n");
        return 0;
    }

/// making combination

    for (int i = 0; i <= n; i++)
        c[i][0] = 1;

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= i; j++)
            c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % P;

/// End of making combination
  cout<<"* "<<c[1][1]<<endl;
  cout<<"* "<<c[2][1]<<endl;
  cout<<"* "<<c[2][2]<<endl;

    for (int i = 0; i < n; i++)
    {
        int x;
        scanf("%d", &x);
        x /= 50;
        if (x == 1)
            n1++;
        else
            n2++;
    }

    for (int i = 0; i <= n1; i++)
        for (int j = 0; j <= n2; j++)
            for (int k = 0; k < 2; k++)
                d[i][j][k] = INF;       /// initializing dp

    d[0][0][0] = 0;
    p[0][0][0] = 1;

    set<T> s;
    s.insert(T(0, 0, 0, 0));

    while (!s.empty())
    {
        int x = s.begin()->x;
        int y = s.begin()->y;
        int fl = s.begin()->fl;
        int dist = s.begin()->val;
        int pp = p[x][y][fl];
        s.erase(s.begin());
//        cout<<x<<"  "<<y<<"  "<<fl<<"  "<<dist<<"  "<<pp<<endl;

        if (fl == 0)  /// this bank
        {
            for (int i = 0; i <= KK && i + x <= n1; i++)  /// kk = boat capacity
                for (int j = 0; i + 2 * j <= KK && j + y <= n2; j++)
                    if (i + j > 0)
                    {
                        if (d[i + x][j + y][fl ^ 1] >= dist + 1)
                        {
                            if (d[i + x][j + y][fl ^ 1] > dist + 1)
                            {
                                s.erase(T(i + x, j + y, fl ^ 1, d[i + x][j + y][fl ^ 1]));
                                d[i + x][j + y][fl ^ 1] = dist + 1;
                                p[i + x][j + y][fl ^ 1] = f(pp, i, n1 - x, j, n2 - y);
                                cout<<pp<<" "<<i<<" "<<n1-x<<" "<<j<<" "<<n2-y<<endl;
                                cout<<">> "<<f(pp, i, n1 - x, j, n2 - y)<<endl;
                                s.insert(T(i + x, j + y, fl ^ 1, d[i + x][j + y][fl ^ 1]));
                            }
                            else
                            {
                                p[i + x][j + y][fl ^ 1] += f(pp, i, n1 - x, j, n2 - y);
                                p[i + x][j + y][fl ^ 1] %= P;
                            }
                        }
                    }
        }

        else   /// oposit bank
        {
            for (int i = 0; i <= KK && i <= x; i++)
                for (int j = 0; i + 2 * j <= KK && j <= y; j++)
                    if (i + j > 0)
                    {
                        if (d[x - i][y - j][fl ^ 1] >= dist + 1)
                        {
                            if (d[x - i][y - j][fl ^ 1] > dist + 1)
                            {
                                s.erase(T(x - i, y - j, fl ^ 1, d[x - i][y - j][fl ^ 1]));
                                d[x - i][y - j][fl ^ 1] = dist + 1;
                                p[x - i][y - j][fl ^ 1] = f(pp, i, x, j, y);
                                s.insert(T(x - i, y - j, fl ^ 1, d[x - i][y - j][fl ^ 1]));
                            }
                            else
                            {
                                p[x - i][y - j][fl ^ 1] += f(pp, i, x, j, y);
                                p[x - i][y - j][fl ^ 1] %= P;
                            }
                        }
                    }
        }
    }

    if (d[n1][n2][1] == INF)
        printf("-1\n0\n");
    else
        printf("%d\n%d\n", d[n1][n2][1], p[n1][n2][1]);
    return 0;
}
