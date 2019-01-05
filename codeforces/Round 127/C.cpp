#include<stdio.h>
#include<string.h>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<stdlib.h>

using namespace std;

struct data
{
    long long co,seq;
};

long long n,space,low,hi;
vector<data> cost;
vector<long long>ll,hh;

bool com(data a, data b)
{
    return (a.co< b.co);
}

int main()
{
    scanf(" %I64d %I64d",&n,&space);
    scanf(" %I64d %I64d",&low,&hi);

    for(int i=0; i<n; i++)
    {
        long long Aa,Bb;
        scanf(" %I64d %I64d",&Aa,&Bb);
        ll.push_back(Aa);
        hh.push_back(Bb);
    }

    for(int i=0; i<n; i++)
    {
        data tmp;
        tmp.co=(ll[i]*low)+(hh[i]*hi);
        tmp.seq=i+1;
        cost.push_back(tmp);
    }
    sort(cost.begin(),cost.end(),com);

    vector<long long> VV;

    long long use=0,serve=0;
    while(use<space && serve<n)
    {
        use+=cost[serve].co;
        if(use>space) break;
        VV.push_back(cost[serve].seq);
        serve++;

    }

    printf("%I64d\n",serve);
    for(int i=0; i<VV.size(); i++)
    {
        printf("%I64d ",VV[i]);
    }
    printf("\n");

    return 0;
}

