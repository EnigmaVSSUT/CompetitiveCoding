#include<stdio.h>
int factorial(int);
int main()
{
	int no,c;
	printf("Enter the number:\n");
	scanf("%d",&no);
	c=factorial(no);
	printf("Factorial =%d\n",c);
	return 0;
}
int factorial(int a)
{
	int f;
	if(f==1||f==0)
	return 1;
	f=a*factorial(a-1);
	return f;
}
