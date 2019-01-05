#include<stdio.h>
#include<algorithm>
#include<map>
#include<vector>
#include<math.h>


using namespace std;

int main()
{
    int n,k,tmp;

    vector<int> vec;
    vec.clear();

    scanf(" %d %d",&n,&k);

    for(int i=0;i<n;i++)
    {
        scanf(" %d",&tmp);
        vec.push_back(tmp);
    }

    sort(vec.begin(),vec.end());

    if(n<k) printf("-1\n");
    else
    {
        printf("%d 0\n",vec[vec.size()-k]);
    }

    return 0;
}
