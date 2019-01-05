#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    int a,b,c,Min;
    while(scanf(" %d %d %d",&a,&b,&c)==3){
    Min=min(a,min(b,c));

    long long ans=0;

    ans+=Min;

    ans+=(a-Min)/3;
    ans+=(b-Min)/3;
    ans+=(c-Min)/3;

    printf("%I64d\n",ans);

    }
    return 0;

}
