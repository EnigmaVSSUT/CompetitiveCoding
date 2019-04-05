#include<iostream>
using namespace std;
int main()
{
    int i,j,k=0;
    for(i=1;i<=7;i+=2)
    {
        for(j=1;j<=k;j++)
            cout<<" ";
            for(j=7;j>=i;j--)
            if(j==7||j==i)
                cout<<"*";
            else
                cout<<" ";
            k++;
        cout<<endl;
    }
    k=2;
    for(i=3;i<=7;i+=2)
    {
        for(j=k;j>=1;j--)
            cout<<" ";
        for(j=1;j<=i;j++)
        if(j==1||j==i)
            cout<<"*";
        else
            cout<<" ";
        cout<<endl;
        k--;
    }
    return 0;
}
