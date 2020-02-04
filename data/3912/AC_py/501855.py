# coding=utf-8
a=int(input())
i=2
for i in range(2,a):
      if a%i==0:
       print('not prime')
       break
else:
       print('prime')