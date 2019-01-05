#include<stdio.h>
#include<map>
#include<iostream>
#include<string.h>
#include<math.h>
#include<string>
#include<algorithm>

using namespace std;

map<int, int>mp;

int primes[1250];
bool num[10005];

int seive(int size)
{
    primes[0]=2;
    int i,j,k,l;
    for(i=3,j=0;i<size;i+=2)
    {
        if(!num[i])
        {
            primes[++j]=i;

            if(i<=size/i)
            {
                k=i*2;
                for(l=i*i;l<size;l+=k) num[l]=true;
            }

        }
    }
    return j+1;
}

string multiplication(string ans,int val)
{
    int i, c=0;
    for(i=0;i<(ans.size());i++)
    {
        c += (ans[i]-'0')*val;
        ans[i] = (c%10 +'0');
        c /= 10;
    }
    while(c)
    {
        ans += (c%10 + '0');
        c /= 10;
    }
    return ans;
}

int Take_To_Pow(int base,int to)
{
    if(to==1) return base;
    if(to==0) return 1;
    int ret=1;

    while(to)
    {
        if(to%2) ret=base*ret;
        base=base*base;
        to/=2;
    }
    return ret;
}

int main()
{
    int T,N,tmp;
    scanf(" %d",&T);
    int nump=seive(10002);

    for(int tt=1;tt<=T;tt++)
    {
        mp.clear();
        scanf(" %d",&N);

        for(int XX=0;XX<N;XX++)
        {
            scanf(" %d",&tmp);

            int lim=sqrt(tmp)+1;

            for(int i=0;primes[i]<=lim;i++)
            {
                if(tmp%primes[i]==0)
                {
                    int freq=0;
                    while(tmp%primes[i]==0)
                    {
                        tmp/=primes[i];
                        freq++;
                    }

                    if(mp[primes[i]]<freq) mp[ primes[i]]=freq;
                }
            }
            if(tmp>1 && mp[tmp]<1)  mp[tmp]=1;
        }
        string ans="1";
        map<int,int>:: iterator it;

        for(it=mp.begin();it!=mp.end();it++)
        {
            int value=Take_To_Pow(it->first,it->second);
            ans=multiplication(ans,value);
        }
        printf("Case %d: ",tt);
        reverse(ans.begin(),ans.end());
        cout<<ans<<endl;
    }
    return 0;
}
