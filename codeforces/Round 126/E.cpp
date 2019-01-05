#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<queue>
#include<stdlib.h>

using namespace std;

int main()
{
    int n,total, fi=0,fj=0,fk=0,tmp;
    scanf(" %d %d",&n,&total);
    for(int i=0; i<n; i++)
    {
        scanf(" %d",&tmp);
        if(tmp==3) fk++;
        else if(tmp==4) fj++;
        else fi++;
    }
    int flag=0;
    int fini,finj,fink,com=99999999;

    for(int i=(total-fk-fj); i>=1; i--)
    {
        for(int j=(total/2); j>=1; j--)
        {
            if(i>=j)
            {
                for(int k=(total/3); k>=1; k--)
                {
                    if( j>=k)
                    {
                        if(((i*fi)+(j*fj)+(k*fk))==total)
                        {
                            if((abs((j*fj)-(i*fi))+abs((k*fk)-(j*fj)))<com)
                            {
                                com=(abs((j*fj)-(i*fi))+abs((k*fk)-(j*fj)));
                                fini=i;
                                finj=j, fink=k;
                            }
                            flag=1;
                        }
                    }
                }
            }
//            if(flag) break;
        }
//        if(flag) break;
    }
    if(flag) printf("%d %d %d\n",fink,finj,fini);
    else if(!flag) printf("-1\n");
    return 0;
}
