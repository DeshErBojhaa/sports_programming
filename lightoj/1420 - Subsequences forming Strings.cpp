#include<stdio.h>
#include<iostream>
#include<string.h>
#include<string>
#include<vector>

using namespace std;

typedef int ll;

int T,as,bs,cs,var,visit[101][101][101][3];
int dp[101][101][101][3],mod=1000000007;
vector<int>nxf[27],nxs[27];
string a,b,c;

ll rec(int ai,int bi,int ci,int konta)
{
     // printf("%d %d %d\n",ai,bi,ci);
     if(ci==cs) return 1;
     //if(ai>=as || bi>=bs) return 0;

     ll &ret=dp[ai][bi][ci][konta];
     if(visit[ai][bi][ci][konta]==var) return ret;
     ret=0;
     visit[ai][bi][ci][konta]=var;

     int ind=(int)(c[ci]-'a');

    if(konta!=2)
     for(int i=0; i<nxf[ind].size(); i++)
     {
          if(nxf[ind][i]>ai)
          {
               ret=(ret+rec(nxf[ind][i],bi,ci+1,0))%mod;
               ret=(ret+rec(nxf[ind][i],bi,ci,1))%mod;
               break;
          }
     }

    if(konta!=1)
     for(int i=0; i<nxs[ind].size(); i++)
     {
          if(nxs[ind][i]>bi)
          {
               ret=(ret+rec(ai,nxs[ind][i],ci+1,0))%mod;
               ret=(ret+rec(ai,nxs[ind][i],ci,2))%mod;
               break;
          }
     }

     return ret;
}

int main()
{
     scanf(" %d",&T);
     for(int tt=1; tt<=T; tt++)
     {
          var++;
          for(int i=0; i<=26; i++)
          {
               nxf[i].clear();
               nxs[i].clear();
          }

          cin>>a>>b>>c;

          as=a.size();
          bs=b.size();
          cs=c.size();

          for(int i=0; i<as; i++)
          {
               for(int j=0; j<26; j++)
               {
                    if(a[i]==char('a'+j))
                         nxf[j].push_back(i+1);
               }
          }
          for(int i=0; i<bs; i++)
          {
               for(int j=0; j<26; j++)
               {
                    if(b[i]==char('a'+j))
                         nxs[j].push_back(i+1);
               }
          }

          ll ans=rec(0,0,0,0);

          printf("Case %d: %d\n",tt,ans);
     }
     return 0;
}
