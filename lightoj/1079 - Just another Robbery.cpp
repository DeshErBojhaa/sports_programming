#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>

using namespace std;

int taka[101],n,cass=0;
double dp[101][10001],prob[101],lim;
int vis[101][10001];

double rec(int cur,int must_take)
{
    if(must_take<=0) return 0.0;
    if(cur==n) return (must_take==0)?0.0:1.0;

    double &ret=dp[cur][must_take];
    if(vis[cur][must_take]==cass) return ret;
    vis[cur][must_take]=cass; ret=(double) 999999999;

    ret=(double)rec(cur+1,must_take-taka[cur])+((1-rec(cur+1,must_take-taka[cur]))*(prob[cur]));
    ret=min(ret,rec(cur+1,must_take));

    return ret;
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf(" %lf %d",&lim,&n);
        for(int i=0;i<n;i++) scanf(" %d %lf",&taka[i],&prob[i]); int high=0,low=0,ans=0;
        for(int i=0;i<n;i++) high+=taka[i];
        cass++;
        while(high>low) /// this gives me WA :(  But  if i use    while(high>=low)  i get Ac
        {
            int mid=(high+low)/2;
            double probability=rec(0,mid);
            if(probability>lim) high=mid-1;
            else low=mid+1;
        }
        printf("Case %d: %d\n",t,low);
    }
    return 0;
}
