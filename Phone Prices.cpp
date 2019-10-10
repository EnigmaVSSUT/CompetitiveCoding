#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int i=0,j,x,min,c=1;
		cin>>x;
		int a[x];
		for(i=0;i<x;i++)
		{
			cin>>a[i];
		}
		for(i=1;i<x;i++)
		{
			min=a[i];
			for(j=i;(j>=i-5)&&(j>=0);j--)
			{
				if(a[i]>a[j])
				{
					min=a[j];
				}
			}
			if(min==a[i])
			c++;
		}
		cout<<c;
	}
}
