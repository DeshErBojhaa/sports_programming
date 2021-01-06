#include<stdio.h>
#include<algorithm>

using namespace std;

int big_prime[100009],ans[100009];

int main()
{
    for(int i=2;i<=100002;i++)
    {
        if(big_prime[i]==0)
        for(int j=i;j<100003;j+=i)
        big_prime[j]=i;
    }

    int n,use,seed,len_sofar;
    scanf(" %d",&n);

    for(int qq=0;qq<n;qq++)
    {
        scanf(" %d",&seed);
        len_sofar=0;

        use=seed;

        while(use>1)
        {
            int prime=big_prime[use];

            if(ans[prime]>len_sofar)
            len_sofar=ans[prime];

            use=use/prime;
        }

        use=seed;

        while(use>1)
        {
            int prime=big_prime[use];
            ans[prime]=len_sofar+1;
            use=use/prime;
        }

    }

    int ret=1;
    for(int i=0;i<100003;i++)
    ret=max(ret,ans[i]);

    printf("%d\n",ret);

    return 0;
}
