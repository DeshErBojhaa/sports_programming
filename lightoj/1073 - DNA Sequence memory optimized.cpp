#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

int T,cs,n,dp[15][1<<15],flag[15][1<<15],onkboro=99999999,addmat[16][16],indd;
string strarr[15];

int find_match(int frn,int bac)
{
    string str=strarr[bac]+"#"+strarr[frn];

    int par[202];
    memset(par,0,sizeof par);
    int k=0,match=0;

    for(int ii=1; ii<str.size(); ii++)
    {
        while(k>0 && str[ii]!=str[k]) k=par[k-1];
        if(str[ii]==str[k]) k++;
        par[ii]=k;
    }
    match=par[str.size()-1];

    return match;
}

bool fullin(int big,int sml)
{
    string str=strarr[sml]+"#"+strarr[big];

    int par[202];
    memset(par,0,sizeof par);
    int k=0;

    for(int ii=1; ii<str.size(); ii++)
    {
        while(k>0 && str[ii]!=str[k]) k=par[k-1];
        if(str[ii]==str[k]) k++;
        par[ii]=k;
        if(k==strarr[sml].size()) return true;
    }
    return false;
}

void process()
{
    bool fff[16];
    memset(fff,false,sizeof fff);
    memset(addmat,0,sizeof addmat);

    sort(&strarr[0],&strarr[n]);

    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
        {
            if(i==j) continue;
            if(fullin(j,i) && !fff[i] && !fff[j])
            {
                fff[i]=true;
                break;
            }
        }

    int ind=0;
    for(int i=0; i<n; i++)
        if(!fff[i]) strarr[ind++]=strarr[i];
    n=ind;
    sort(&strarr[0],&strarr[n]);

    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
        {
            if(i==j) continue;
            int match=find_match(i,j);
            addmat[i][j]=strarr[j].size()-match;
        }

    return;
}

int rec(int last,int mask)
{
    if(__builtin_popcount(mask)==n) return 0;
    int &ret=dp[last][mask];
    if(flag[last][mask]==cs) return ret;
    ret=onkboro;
    flag[last][mask]=cs;

    for(int i=0; i<n; i++)
    {
        if((mask&(1<<i))==0)
        {
            int jogg=(addmat[last][i]);
            ret=min(ret,rec(i,mask|(1<<i))+jogg);
        }
    }
    return ret;
}

string path(int last,int mask)
{
    if(__builtin_popcount(mask)==n) return "";
    int &ret=dp[last][mask],nc;

    string ssttrr="";
    for(int i=0; i<n; i++)
    {
        if((mask&(1<<i))==0)
        {
            int val=((int)strarr[last].size())-addmat[last][i];

            if(val+rec(i,mask|(1<<i))==ret)
            {
                string tmp=strarr[i].substr(addmat[last][i]);
                if(ssttrr=="" || tmp<ssttrr)
                {
                    nc=i;
                    ssttrr=tmp;

                }

            }
        }
    }
    string fin=strarr[last].substr((addmat[last][nc]));
    fin+=path(nc,mask|(1<<nc));
    return fin;
}

int main()
{
    scanf(" %d",&T);
    for(cs=1; cs<=T; cs++)
    {
        scanf(" %d",&n);
        for(int i=0; i<n; i++)
            cin>>strarr[i];
        int ball=onkboro;

        process();

        for(int i=0; i<n; i++)
        {
            int hudai=rec(i,(1<<i));
            if(hudai<ball)
            {
                ball=hudai;
                indd=i;
            }
        }

        printf("Case %d: ",cs);

        cout<<path(indd,(1<<indd))<<endl;

    }
    return 0;
}

// GTGCAACAGTATGCTAAACTTATCTTCCCCGATCTTGTCGGAAATGGCTATTATTCTGA
// GTGCAACAGTATGCTAAACTTATCTTCCCCGATCTTGTCGGAAATGGCTATTATTCTGA
