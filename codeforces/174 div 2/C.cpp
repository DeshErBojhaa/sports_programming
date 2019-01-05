#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<iostream>
#include<vector>
#include<queue>
#include<math.h>
#include<sstream>

using namespace std;

int len=0;
double total=0.0;
int last=0;
vector<long long>vec;


int main()
{
    int n,opa,to,h,no;
    vec.push_back(0);

    cin>>n;
    for(int i=0;i<n;i++)
    {
        scanf(" %d",&opa);
        if(opa==1)
        {
            scanf(" %d %d",&to,&no);

            for(int i=0;i<to;i++)
            {
                vec[i]+=no;
                total+=(no*1.0);
            }

        }
        else if(opa==2)
        {
            scanf(" %d",&no);

            total+=no;
            vec.push_back(no);
        }
        else
        {
            int len=vec.size()-1;
            total-=vec[len];
            vec.pop_back();
        }

        double avg;
        if((int)vec.size())
        avg=(total*1.0)/(1.0* (vec.size()));
        else
        avg=0.0;
        printf("%.7lf\n",avg);
    }

    return 0;
}
