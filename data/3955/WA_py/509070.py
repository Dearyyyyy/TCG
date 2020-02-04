# coding=utf-8
while True:
   a,b=input().split()
   l=len(a)
   for i in range(l-1):
       a=a[-1]+a[:-1]
       if b==a:
          print('Yes')
else:
    print('No')