#include<stdio.h>
#include<queue>
#include<string.h>
#include<algorithm>
#include<vector>
#include<math.h>

using namespace std;

#define me(a,b) memset(a, b,sizeof(a))
#define pr printf("Case %d: ",t)
#define sc scanf(" %d",&tt)
#define lp for(int t=1;t<=tt;t++)
#define Lp for(int i=1; i<=1000; i++)
#define re return

int iii[1001];
bool p[1001];
vector<int>V[1001];
const int prime[]= {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,
                    107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,
                    199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,
                    317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,
                    443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,
                    577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,
                    701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,
                    839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,
                    983,991,997
                   };


void lenjur()
{
    Lp
    {
        int now=i;
        for(int j=0; prime[j]*prime[j]<=i+1; j++)
        {
            if(now%prime[j]==0)
            {
                while(now%prime[j]==0)
                    now=now/prime[j];
                V[i].push_back(prime[j]);
            }
        }
        if(now>1 && now!=i)
            V[i].push_back(now);
    }
    re;
}

int bfs(int ii, int e)
{
    queue<int>Q;
    Q.push(ii);
    while(!Q.empty())
    {
        ii=Q.front();
        p[ii]=true;
        Q.pop();
        if(ii==e)
            re iii[ii];
        for(int i=0; i<V[ii].size(); i++)
        {
            if((ii+(V[ii][i]))<=e)
            {
                if(!p[(ii+V[ii][i])])
                {
                    Q.push(ii+V[ii][i]);
                    p[ii+(V[ii][i])]=true;
                    iii[ii+(V[ii][i])]=iii[ii]+1;
                }
                if((ii+(V[ii][i]))==e)
                    re iii[ii+(V[ii][i])];
            }
        }
    }

    return -1;
}

int main()
{
    lenjur();
    int tt,b,e;
    sc;
    lp
    {
        me(iii, 0);
        me(p, false);
        scanf(" %d %d",&b,&e);
        pr;
        printf("%d\n",bfs(b,e));
    }
    return 0;
}
