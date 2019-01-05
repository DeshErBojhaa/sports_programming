#include<stdio.h>
#include<string.h>
#include<string>
#include<iostream>

using namespace std;

int nim[101];
string str;

int find_nim(int in)
{
    if(in==0 ) return nim[in]=0;
    bool flag[101];
    if(nim[in]!=-1) return nim[in];
    nim[in]=0;
    for(int i=0; i<in; i++)
    {
        int ind=find_nim(i) ^ find_nim(in-i-1);
        flag[ind]=true;
    }
    int i=0;
    for(i=0;; i++) if(flag[i]==false) break;
    nim[in]=i;
    return nim[in];
}

int main()
{
    memset(nim,-1,sizeof nim);
    int T;
    scanf(" %d",&T);
    for(int t=1; t<=T; t++)
    {
        int cnt=0,last=0,ch=0,ans=0;
        cin>>str;

        for(int i=0; i<str.size(); i++)
        {
            if(str[i]!='.') cnt++;
            else ch++;

            if(last==0 && str[i]!='.')
            {
                ans^=find_nim(ch);
                cout<<"HUDA "<<ch<<endl;
                ch=0;
                if(str[i]=='X') last=1;
                else last=2;
            }
            else
            {
                if((str[i]=='X' && last==1) || ( str[i]=='O' && last==2))
                {
                    if(ch%2)
                    {
                        ans^=find_nim(ch);
                        cout<<"call "<<ch<<endl;
                    }
                    else
                    {
                        ans^=find_nim(ch-1);
                        cout<<"ball call "<<ch-1<<endl;
                    }
                    ch=0;
                }
                if((str[i]=='X' && last==2) || (str[i]=='O' && last==1))
                {
                    if(ch%2)
                    {
                        ans^=find_nim(ch-1);
                        cout<<"CALL "<<ch-1<<endl;
                    }
                    else
                    {
                        ans^=find_nim(ch);
                        cout<<"CALL "<<ch<<endl;
                    }
                    ch=0;
                }
            }


        }
        cout<<"Last Call "<<ch<<endl;
        ans^=find_nim(ch);

        ///if(cnt%2) ans=!ans;

        if(ans) printf("Case %d: Yes\n",t);
        else printf("Case %d: No\n",t);
    }
    return 0;
}


/*






            */
