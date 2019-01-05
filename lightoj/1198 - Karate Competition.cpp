#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;

vector<int>me,op;

int main()
{
    int T,N;
    scanf(" %d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        me.clear();
        op.clear();
        scanf(" %d",&N);
        for(int i=0;i<N;i++)
        {
            int tm;
            scanf(" %d",&tm);
            me.push_back(tm);
        }
        for(int i=0;i<N;i++)
        {
            int tm;
            scanf(" %d",&tm);
            op.push_back(tm);
        }
        sort(me.begin(),me.end());
        sort(op.rbegin(),op.rend());

        int opind=0;
        int ans=0;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
                if(me[i]>op[j] && op[j]>0) {ans+=2;me[i]=-111;op[j]=-99;break;}
        }

        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++) if(me[i]==op[j]) {ans++;op[j]=-99;break;}

        }
        printf("Case %d: %d\n",tt,ans);
    }
    return 0;
}
