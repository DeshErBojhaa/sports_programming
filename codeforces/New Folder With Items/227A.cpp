#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;

int ax,ay,bx,by,cx,cy;

int main()
{
    scanf(" %d %d %d %d %d %d",&ax,&ay,&bx,&by,&cx,&cy);
    long long vec1x=ax-bx;
    long long vec1y=ay-by;

    long long vec2x=ax-cx;
    long long vec2y=ay-cy;

    long long ball=(vec1x*vec2y)-(vec1y*vec2x);

    if(ball==0) printf("TOWARDS\n");
    else if(ball>0) printf("LEFT\n");
    else printf("RIGHT\n");
}
