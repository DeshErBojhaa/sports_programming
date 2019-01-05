#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<string>
#include<map>
#include<iostream>
#include <sstream>

using namespace std;

struct data
{
    int next_ref[58];
    int end_here;
};

data arr[100002];
string str,line;
int N;

void clear_trie(int i)
{
    arr[i].end_here=0;
    memset(arr[i].next_ref,-1,sizeof arr[i].next_ref);
    return;
}

void build_trie(int cur_pos,int cur_leaf)
{
    if(((int)str.size())==cur_pos)
    {
        arr[cur_leaf].end_here++;
        return;
    }

    int index;

    if(str[cur_pos]>='a')
        index=27+str[cur_pos]-'a';
    else
        index=str[cur_pos]-'A';

    int &next_leaf=arr[cur_leaf].next_ref[index];

    if(next_leaf==-1)
    {
        clear_trie(++N);
        next_leaf=N;
    }

    build_trie(cur_pos+1,next_leaf);

    return;
}

int find_trie(int cur,int node)
{
    if(cur==((int)str.size()))
    {
        return arr[node].end_here;
    }

    int index;
    if(str[cur]>='a')
        index=27+str[cur]-'a';
    else
        index=str[cur]-'A';

    int &next_node=arr[node].next_ref[index];

    if(next_node==-1) return 0;
    else return find_trie(cur+1,next_node);
    return 0;
}

char word[110];
char lne[100010];

int main()
{
    int T,no_w,no_s;
    scanf(" %d",&T);

    for(int tt=1; tt<=T; tt++)
    {
        clear_trie(0);
        N=0;
        scanf(" %d",&no_w);
        for(int i=0; i<no_w; i++)
        {
            scanf(" %s", &word);
            str = word;
            if(str.size()>3)
            {
                sort(str.begin()+1 , str.end()-1);
            }
            build_trie(0,0);
        }

        int total=1;



        scanf("%d",&no_s);
        char ball;
        scanf("%c",&ball);
        printf("Case %d:\n",tt);
        for(int i=0; i<no_s; i++)
        {
            total=1;
            line="";
            gets(lne);
            line = lne;

            stringstream ss;
            ss.clear();
            ss<<line;
            for(;ss>>str;)
            {
                if(str.size()>3)
                {
                    sort(str.begin()+1, str.end()-1);
                }

                int friq=find_trie(0,0);

                total*=friq;
            }
            printf("%d\n",total);
        }

    }
    return 0;
}


/*

1
8
blowed
bowled
baggers
beggars
int
the
barn
bran

*/
