#include<stdio.h>

#define pf printf

long long fun(int dym, int rook)
{
    long long ans;
    int tem=1,  bem=1;
    for(int i=rook+1;i<=dym;i++)
    {
        tem*=i;
        if(tem%(i-rook)==0)
        tem=tem/(i-rook);
        else
        {
            bem*=(i-rook);
        }
    }
    ans=tem/bem;
//    pf("Ans %lld\n",ans);
    return ans;
}


int main()
{
    int T,dym,rook;
    long long comb,rook_comb;
    scanf("%d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf("%d %d",&dym,&rook);
        pf("Case %d: ",tt);
        comb=1;
        for(int i=0;i<rook;i++)
        {
            comb*=(dym-i);
        }
//        pf("comb %lld\n",comb);
        rook_comb=fun(dym,rook);
        printf("%lld\n",rook_comb*comb);

    }
    return 0;
}
