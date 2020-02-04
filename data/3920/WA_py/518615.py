# coding=utf-8
#include<cstdio>
int main()
{
	int a,b,c,m,n;
	while(scanf("%d",&m)!=EOF)
	{
		a=m/100;
		b=m%100/10;
		c=m%10;
	//	printf("%d %d %d",a,b,c);
		if(m==a*a*a+b*b*b+c*c*c)
			printf("Yes\n");
		else
			printf("No\n");
	}
	return 0;
}