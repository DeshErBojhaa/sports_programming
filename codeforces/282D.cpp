#include<stdio.h>
#include<algorithm>
#include<iostream>

using namespace std;

bool dp[301][301];

void make_dp()
{
    for(int i=0;i<301;i++)
    {
        for(int j=max(i,1);j<=300;j++)
        {
            for(int ii=0;ii<i;ii++)
            {
                if(dp[ii][j]==false)
                {
                    dp[i][j]=true;
                    break;
                }
            }
            for(int jj=0;jj<j and dp[i][j]==false ;jj++)
            {
                if(dp[i][jj]==false)
                {
                    dp[i][j]=true;
                    break;
                }
            }
            for(int kk=1;kk<=min(i,j) and dp[i][j]==false; kk++)
            {
                if(dp[i-kk][j-kk]==false)
                {
                    dp[i][j]=true;
                    break;
                }
            }
            dp[j][i]=dp[i][j];
        }
    }
    return;
}

int main()
{
    int n;
    cin>>n;

    if(n==1)
    {
        int tmp;
        cin>>tmp;
        if(tmp) cout<<"BitLGM"<<endl;
        else cout<<"BitAryo"<<endl;
    }
    if(n==2)
    {
        make_dp();
        for(int i=0;i<20;i++)
        {
            for(int j=0;j<20;j++)
            if(dp[i][j]) printf("1 ");
            else cout<<"0 ";
            cout<<endl;
        }
        int a,b;
        cin>>a>>b;
        if(dp[a][b]) cout<<"BitLGM"<<endl;
        else cout<<"BitAryo"<<endl;
    }
    else
    {
        int a,b,c;
        cin>>a>>b>>c;
        if(a^b^c) cout<<"BitLGM"<<endl;
        else cout<<"BitAryo"<<endl;
    }

    return 0;
}
