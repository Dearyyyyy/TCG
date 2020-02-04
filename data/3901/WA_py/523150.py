# coding=utf-8
#include<stdio.h>
int main ()
{
   int N,a=1,b=1,c=0;
   scanf("%d",&N);
   for(int i=N-1;i>=1;i--)
   {
   	 a=(a+1)*2;
   	 b=2*(1 + b);
   }
   printf("%d",b);
	return 0;
}