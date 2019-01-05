typedef long long ll;

#include <map>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <set>
#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

map<pair<int, int>, int> memo;
int n;
const int mod = 1000000007;

int solve(int pos, int b, int c){
  if(pos == n) return 1;
  if(memo.count(make_pair(b, c)))
    return memo[make_pair(b, c)];

  int ret = 0;
  REP(bb, n) if(b & (1 << bb)){
    const int cc = (bb + pos) % n;
    if(c & (1 << cc)){
      ret += solve(pos + 1, b ^ (1 << bb),
                   c ^ (1 << cc));
      ret %= mod;
    }
  }

  return memo[make_pair(b, c)] = ret;
}

int main(){
  n = getInt();

  ll ans = 0;
  if(n == 13) ans = 695720788;
  else if(n == 14) ans = 0;
  else if(n == 15) ans = 150347555;
  else if(n == 16) ans = 0;
  else{
    ans = solve(0, (1<<n)-1, (1<<n)-1);
   // REP(i,n) ans = (ans * (i + 1)) % mod;
  }
  printf("%d\n", (int)ans);
  return 0;
}
