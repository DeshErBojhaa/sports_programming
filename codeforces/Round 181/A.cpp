#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<math.h>
#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int n,poss,negg;
    cin>>n;
    bool pos=false;
    bool neg=false;
    bool zer=false;

    vector<int>vec,minus,zero;


    for(int i=0; i<n; i++)
    {
        int tmp;
        scanf(" %d",&tmp);

        if(tmp==0)
        {
            zero.push_back(tmp);
        }
        if(tmp>0)
        {
             vec.push_back(tmp);
        }
        if(tmp<0)
        {
            if(neg==false)
            {
                neg=true;
                negg=tmp;
            }
            else
                vec.push_back(tmp);
        }

    }

     printf("1 %d\n",negg);
     printf("%d",(int)vec.size());
     for(int i=0;i<vec.size();i++) printf(" %d",vec[i]);
     cout<<endl;
     printf("%d",(int)zero.size());
     for(int i=0;i<zero.size();i++) printf(" %d",zero[i]);
     cout<<endl;

    return 0;
}
