# coding=utf-8
char str[999]
  while(scanf("%s",str)!=EOF):
  
  for(i=0;str[i]!='\0';i++)
  if(str[i]=='Y'):
   if(str[i-1]=='1'):
   
	s=s+1
   
   if(str[i-1]=='2'):
     e=e+2
	
   if(str[i-1]=='3'):
    f=f+3
	
	
  
  if(str[i]=='R'):
   {a=a+1;}
   if(str[i]=='A'):
   b=b+1
	 
	if(str[i]=='S'):
	c=c+1
	if(str[i]=='B'):
	d=d+1
	
	
	if(str[i]=='2'):
	x=x+1;
	 if(str[i+1]=='Y'):
	 {y=y+1;}
	 z=x-y; 
	
	if(str[i]=='3'):
	h=h+1;
	 if(str[i+1]=='Y'):
	   k=k+1;
		
		l=h-k;
	
	if(str[i]=='1'):
	p=p+1;
	 if(str[i+1]=='Y'):
	  m=m+1;
	  
	  n=p-m;
	
	if(str[i]=='T'):
	  {r=r+1;} 
	  
	  
	  q=s+e+f+a+b+c+d-z-n-r-l
   
	  
	  printf("%d\n",s+e+f+a+b+c+d-z-n-r-l)