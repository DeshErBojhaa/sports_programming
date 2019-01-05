#include "iostream"
#include "iomanip"
#include "cstdio"
#include "algorithm"
#include "string"
#include "cmath"
#include "cstring"
#include "vector"

#define ll long long
#define ld long double

using namespace std;

//#define p(t) { printf("Line: %4d  %15s = ", __LINE__, # t); cout << t << endl; };
#define p(t) ;

vector<int> v[100005];

bool neigh(int a, int b) {
	for (int i = 0; i < 4; ++i)
	{
		if (v[a][i] == b) return true;
	}
	return false;
}

int main()
{

	int n;

	cin >> n;

	//pair<int, int> p[200005];

	for (int i = 0; i < n*2; ++i)
	{
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}

	for (int i = 1; i <= n; ++i)
	{
		if (v[i].size() != 4) {
			//cout << i;
			cout << -1 << endl;
			return 0;
		}
	}

	if (n == 5) {
		cout << "1 2 3 4 5" << endl;
		return 0;
	}

	int r[100005] = {};
	if (n == 6) {
		r[0] = 1;
		for (int j = 2; j <= 6; ++j)
		{
			if (!neigh(1, j)) {
				r[3] = j;
			}
		}
		for (int i = 0; i < 2; ++i)
		{
			int c = v[1][i];
			r[i+1] = c;
			for (int j = 1; j <= 6; ++j)
			{
				if (c != j && !neigh(c, j)) {
					r[i+4] = j;
				}
			}
		}
		bool ch[7] = {};
		for (int i = 0; i < 6; ++i)
		{
			if (ch[r[i]]) {
				cout << -1 << endl;
				return 0;
			}
			ch[r[i]] = true;
		}


	for (int i = 0; i < n; ++i)
	{
		cout << r[i] << ' ';
	}
	cout << endl;

		return 0;
	}
	/// endof 6

	int third = -1;
	r[0] = 1;

	int s[4] = {};

	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (neigh(v[1][i], v[1][j])) {
				s[i]++;
			}
		}
	}

	bool good = false;

	for (int i = 0; i < 4 && !good; ++i)
	{
		p(s[i])
		p(v[1][i])
		if (s[i] == 1) {
			for (int j = 0; j < 4; ++j)
			{
				if (s[j] == 2) {
					if (neigh(v[1][i], v[1][j])) {
						good = true;
						r[1] = v[1][j];
						r[2] = v[1][i];
					}
				}
			}
		}
	}


	if (!good) {
		p(good)
		cout << -1 << endl;
		return 0;
	}


	for (int i = 3; i < n; ++i)
	{
		p(i)
		int n1 = 0;
		int n2 = 0;
		for (int k = 0; k < 4; ++k)
		{
			if (v[r[i-1]][k] != r[i-2] && v[r[i-1]][k] != r[i-3])
				n1 = v[r[i-1]][k];
		}
		for (int k = 3; k >= 0; --k)
		{
			if (v[r[i-1]][k] != r[i-2] && v[r[i-1]][k] != r[i-3])
				n2 = v[r[i-1]][k];
		}
		p(n1)
		p(n2)
		p(r[i-2])
		if (neigh(n2, r[i-2])) {
			p(n2)
			p(r[i-2])
			swap(n1, n2);
		}
		r[i] = n1;
	}

	if (!(neigh(r[0], r[n-2]) && neigh(r[0], r[n-1]) && neigh(r[1], r[n-1]))) {
		p("ne")
		cout << -1 << endl;
		return 0;
	}

	for (int i = 0; i < n; ++i)
	{
		cout << r[i] << ' ';
	}
	cout << endl;

	return 0;
}
