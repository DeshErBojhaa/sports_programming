#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<iostream>

using namespace std;

struct data
{
    string a,b,c;
};
data tmp;

int n;
string begin,end,ata,pata,mata;
vector<data> forb;
map<string,int>mp;

bool inv_ck(string str)
{
    int flag=0;
    for(int i=0;i<n;i++)
    {
        flag=0;

        for(int j=0;j<forb[i].a.size();j++)
        if(str[0]==forb[i].a[j]) {flag++;break;}

        for(int j=0;j<forb[i].b.size();j++)
        if(str[1]==forb[i].b[j]) {flag++;break;}

        for(int j=0;j<forb[i].c.size();j++)
        if(str[2]==forb[i].c[j]) {flag++;break;}

        if(flag==3) return true;
    }
    return false;
}

int bfs()
{
//    cout<<" lul"<<endl;
    string base,tmp;

    queue<string>Q;
    Q.push(begin);

    mp[begin]=0;

    while(Q.size())
    {
        base=Q.front(); Q.pop();
        if(base==end) return mp[end];
//        cout<<"while"<<endl;
        for(int i=0;i<3;i++)
        {
//            cout<<"LOOP"<<endl;
            tmp=base;
            tmp[i]++;
            if(tmp[i]>'z') tmp[i]='a';

            if(inv_ck(tmp)==false && mp[tmp]==0)
            {///cout<<"lul\n";
                Q.push(tmp);
                mp[tmp]=mp[base]+1;
            }

            tmp=base;
            tmp[i]--;
            if(tmp[i]<'a') tmp[i]='z';

            if(inv_ck(tmp)==false && mp[tmp]==0)
            {///cout<<"bul\n";
                Q.push(tmp);
                mp[tmp]=mp[base]+1;
            }

        }
    }
    return mp[end];
}

int main()
{
    int T;
    scanf(" %d",&T);
    for(int t=1;t<=T;t++)
    {
        forb.clear();
        mp.clear();

        cin>>begin>>end;
        scanf(" %d",&n);

        for(int i=0;i<n;i++)
        {
            cin>>ata>>pata>>mata;
            tmp.a=ata;
            tmp.b=pata;
            tmp.c=mata;

            forb.push_back(tmp);
        }

        if(inv_ck(begin) || inv_ck(end))
        {
            printf("Case %d: -1\n",t);
            continue;
        }
        if(begin==end)
        {
            printf("Case %d: 0\n",t); continue;
        }
        int ans=bfs();
        if(ans)
        printf("Case %d: %d\n",t,ans);
        else
        printf("Case %d: -1\n",t);
    }
    return 0;
}


