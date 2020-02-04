# coding=utf-8
a=int(input())
for i in range(2,a):
  if a%i==0:
     print('not prime')
     break
  elif i==a-1:
      
      print('prime')