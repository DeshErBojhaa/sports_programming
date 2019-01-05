#include<stdio.h>
#include<algorithm>
#include<map>
#include<vector>
#include<math.h>
#include<string.h>


using namespace std;

struct data

{
    int x,y;
};
data baal;
vector<data>vec;

bool flag[700000];

bool com(data ax,data ay)
{
    if(ax.x==ay.x) return ax.y<ay.y;
    else
    return ax.x<ay.x;
}

int main()
{
    vec.clear();
    memset(flag,false ,sizeof flag);

    int n,xx,yy;

    scanf(" %d",&n);

    for(int i=0;i<(2*n);i++)
    {
        scanf(" %d %d",&xx,&yy);
        baal.x=xx;
        baal.y=yy;
        vec.push_back(baal);


    }

    sort(vec.begin(),vec.end(),com);
///for(int i=0;i<vec.size();i++) printf("** %d %d\n",vec[i].x,vec[i].y);

    printf("%d",vec[0].x);
//    printf(" %d",vec[0].y);
    flag[vec[0].x]=true;
//    flag[vec[0].y]=true;

    for(int i=0;i<vec.size();i++)
    {
        int bb=vec[i].x;
        int mm=vec[i].y;
        if(flag[bb]==false)
        {
            flag[bb]=true;
            printf(" %d",bb);
        }
        if(flag[mm]==false)
        {
            flag[mm]=true;
            printf(" %d",mm);
        }
    }
    printf("\n");
    return 0;
}
