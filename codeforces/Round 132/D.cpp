#include<stdio.h>
#include<string>
#include<string.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<iostream>
#include<math.h>

using namespace std;

int main()
{
    int place,baby;

    scanf(" %d %d",&place,&baby);
    int final_ans=0;

    for(int p=0; p<place; p++)
    {
        int t,T,allu,bus;
        scanf(" %d %d %d %d",&t,&T,&allu,&bus);

        if(T-t<0)
        {
            final_ans=(allu*baby)+bus;

        }
        else
        {
            int d=T-t;
            if(baby%d==0) final_ans+=min((bus*(baby/d)),(allu*baby)+bus);
            else
            final_ans+=min((bus*(baby/d)+1),(allu*baby)+bus);
        }

    }

    printf("%d\n",final_ans);
    return 0;
}
