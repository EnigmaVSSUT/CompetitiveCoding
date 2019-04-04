#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	long long int t, n, a, b ,k,g, lcm,x,y,q;
	cin>>t;
	while(t--)
	{
		cin>>n>>a>>b>>k;
		g=__gcd(a,b);
		lcm=(a*b)/g;
		x= n/a;
		y=n/b;
		q=x+y-(2*lcm);
		
				if(q>=k)
		{
			cout<<"Win\n";
		}
		else
			cout<<"Lose\n";
		
	}
}
