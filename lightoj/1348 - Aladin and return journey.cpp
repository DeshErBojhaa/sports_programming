#include<bits/stdc++.h>
using namespace std;
int N,GenieAtNode[30003],Fenwic[30003],Parent[30003],Ancestor[30003][15];
int Level[30003],InTime[30003],OutTime[30003],ttt;
vector<int>G[30003];
bool flag[33033];
void Update(int ind,int value)
{
     for(; ind<=N; ind+=ind&-ind)
          Fenwic[ind]+=value;
     return;
}
void LcaDfs(int cur,int depth)
{
     /// Setting Entering Time
     InTime[cur] = ++ttt;
     /// Setting Level/Depth of a Node ( Useful in LCA Part)
     Level[cur] = depth;
     flag[cur] = true;
     for(int i=0; i<G[cur].size(); i++)
          if(flag[ G[cur][i] ]==false)
          {
               Parent[ G[cur][i] ] = cur;
               LcaDfs(G[cur][i],depth+1);
          }
     OutTime[cur] = ttt;
     return;
}
void Initialize_LCA()
{
     memset(Ancestor,-1,sizeof Ancestor);
     ttt=0;

     /// This DFS Finds Entering time and Leaving time of a Node
     LcaDfs(1,0);
     for(int i=1; i<=N; i++)
          Ancestor[i][0] = Parent[i];
     for(int j=1; (1<<j)<=N; j++)
          for(int i=1; i<=N; i++)
               if(Ancestor[i][j-1] != -1)
                    Ancestor[i][j]=Ancestor[ Ancestor[i][j-1] ][j-1];
     return;
}
int FindLCA(int p,int q)
{
     int log,tmp;
     if(Level[p]<Level[q]) swap(p,q);
     for(log=1; 1<<log <=Level[p]; log++);
     log--;
     for(int i=log; i>=0; i--)
          if(Level[p]-(1<<i) >= Level[q])
               p = Ancestor[p][i];
     if(p==q) return p;
     for(int i=log; i>=0; i--)
          if(Ancestor[p][i]!=-1 && Ancestor[p][i] != Ancestor[q][i])
               p=Ancestor[p][i],q=Ancestor[q][i];
     return Parent[p];
}
int CumulativeSum(int ind)
{
     int ret=0;
     for(; ind>0; ind-=ind&-ind)
     {
          ret+=Fenwic[ind];
     }
     return ret;
}
int main()
{
     int T,cass=1,Q;
     scanf(" %d",&T);
     while(T--)
     {
          memset(flag,false,sizeof flag);
          /// Parent[30003][15] ; Where Parent[i][j] is the j-th Ancestor of i
          memset(Parent,-1,sizeof Parent);
          /// Fenwic[30003] ; Binary Indexed Tree
          memset(Fenwic,0,sizeof Fenwic);
          scanf(" %d",&N);
          for(int i=0; i<=N; i++) G[i].clear();

          /// My Code is 1 base indexed ( indexing starts from 1)
          for(int i=1; i<=N; i++)
               scanf(" %d",&GenieAtNode[i]);
          for(int i=0; i<N-1; i++)
          {
               int a,b;
               scanf(" %d %d",&a,&b);
               a++;
               b++;   /// My Code is 1 based but Problem statement is 0 based
               G[a].push_back(b);
               G[b].push_back(a);
//               Parent[b] = a;   /// Immediate parent of b ( Needed in LCA calculating)
          }
          Initialize_LCA();
          for(int i=1; i<=N; i++)
          {
               Update(InTime[i],GenieAtNode[i]);
               Update(OutTime[i]+1,-GenieAtNode[i]);
          }
          scanf(" %d",&Q);
          printf("Case %d:\n",cass++);
          while(Q--)
          {
               int a,b,c;
               scanf(" %d %d %d",&a,&b,&c);
               c++;
               b++;
               if(a==0)  /// Query
               {
                    int Lca = FindLCA(b,c);
                    printf("%d\n",CumulativeSum(InTime[b])+CumulativeSum(InTime[c])-
                           2*CumulativeSum(InTime[Lca])+GenieAtNode[Lca]);
               }
               else    /// Update
               {
                    c--;
                    int change = c- GenieAtNode[b];
                    GenieAtNode[b] = c;
                    Update(InTime[b],change);
                    Update(OutTime[b]+1,-change);
               }
          }
     }
     return 0;
}
