# coding=utf-8
while True:
   a,b=input().split()
   l=len(a)
   flag=0
   for i in range(l):
       a=a[-1]+a[:-1]
       if b==a:
          flag=1
          print('Yes')
   if flag==0:
          print('No')