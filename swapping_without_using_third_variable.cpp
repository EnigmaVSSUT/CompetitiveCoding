#include<iostream>
using namespace std;
void method1(int a,int b){
	a=a+b;
	b=a-b;
	a=a-b;
	cout<<"value of a and b after swapping is: "<<a<<" "<<b<<endl;
	
}
void method2(int a,int b){
 //this method will not work if either a or b=0;
	a=a*b;
	b=a/b;
	a=a/b;
	cout<<"value of a and b after swapping is: "<<a<<" "<<b<<endl;
	
}
void method3(int a,int b){
//this method will mot work if both the variables are 0.
	a=a^b;
	b=a^b;
	a=a^b;
	cout<<"value of a and b after swapping is: "<<a<<" "<<b<<endl;
}

int main()
{
	int a,b;
	cin>>a>>b;
//Using Arithmetic Operators
	method1(a,b);
	method2(a,b);
//Using Bitwise XOR
	method3(a,b);
	return 0;
	
	
}
