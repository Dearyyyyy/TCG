# coding=utf-8
#include<stdio.h>
int main()
{
	int s=1,i,N;
	scanf("%d",&N);
	for(i=1;i<N;i++)
	s=2*(s+1);
	printf("%d",s);
	return 0;	
}