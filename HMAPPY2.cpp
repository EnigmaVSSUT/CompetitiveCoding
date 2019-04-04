#include<iostream>
using namespace std;
#include<algorithm>

int main()
{
	long int t,n,a,b,k,w,g;
	cin>>t;
	while(t--)
	{
		cin>>n>>a>>b>>k;
		g=__gcd(a,b);
		w=n/a+n/b+2*(a*b)/g;
		if(w>=k)
			cout<<"Win";
		else
			cout<<"Lose";
	}
}
