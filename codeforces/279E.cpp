#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
    int x=0, y=1;
    char c;
    while(scanf("%c", &c)!=EOF)
        {c=='1'?x=min(x, y)+1:y=min(x, y)+1;
        printf("%c   X => %d   Y => %d\n",c,x,y);
        }
    printf("%d\n", min(x, y));
    return 0;
}
