#include<iostream>
using namespace std;
#include<algorithm>
int main()
{
    long int i,t,n,k,a,b,c,g;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n>>a>>b>>k;
        g=(a*b)/(__gcd(a,b));
        c=(n/a)+(n/b)-(2*(n/g));
        if(c>=k)
            cout<<"\nWin\n";
        else
            cout<<"\nLose\n";
    }
    return 0;
}
