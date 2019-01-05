#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<queue>
#include<map>
#include<string>
#include<iostream>
#include<sstream>
#include<math.h>

using namespace std;

int inp,len;
int dp[15][1<<11];

//void pnt(int mas)
//{
//    while(mas)
//    {
//        if(mas%2) printf("1");
//        else printf("0");
//        mas=mas/2;
//    }
//    printf("\n");
//    return;
//}

int rec(int len,int mask)
{
//    printf("len %d ",len);pnt(mask);
    int match=__builtin_popcount(mask);

    if(match>2) return 0;
    if(len == 0 && match<3) return 1;

    int &ret=dp[len][mask];
    if(ret!=-1) return ret;
    ret=0;


    for(int i=0;i<10;i++)
    {
        int use=mask;
        if((use & (1<<i))==0)
        use=(use | (1<<i));

        ret+=(rec(len-1,use));
    }
    return ret;

}



int calc(int N)
{
    stringstream ss;
    ss.clear();

    string str;

    ss<<N;
    ss>>str;

    int len=str.size();

    int ans=0;

    for(int i=1; i<len; i++)
        for(int j=1; j<10; j++)
            ans+=rec(i-1,(1<<j));


//printf("1 loop %d\n",ans);


    for(int i=1; i<str[0]-'0'; i++)
        ans += rec(len-1 ,(1<<i));


//printf("2 loop %d\n",ans);


    int digit=(str[0]-'0');
    int pre=digit;
    int lim=1,total=0,mask=0,original=0;

    mask=(mask|(1<<pre));
    original=mask;


    for(int i=1; i<len; i++)
    {
        for(int j=0; j<str[i]-'0'; j++)
        {
            mask=original;
            if((mask & (1<<j))==0) {
            mask = (mask|(1<<j));}

            if(__builtin_popcount(mask)>2) continue;

//            printf("len %d   dig %d ",len-i-1,j);(pnt(mask));
            ans+=rec(len-i-1,mask);
//            printf("ANS %d\n",ans);
        }

        int cur=str[i]-'0';
        if((original & (1<<cur))==0) {//lim++;
        original= original|(1<<cur);}

        if(__builtin_popcount(original)>2) break;
//        pre=cur;
    }

    return ans;
}

int main()
{
    scanf(" %d",&inp);
    memset(dp,-1,sizeof dp);

    if(inp<102 && inp>0) printf("%d\n",inp);

    else
    {
        printf("%d\n",calc(inp+1));
    }

    return 0;
}

