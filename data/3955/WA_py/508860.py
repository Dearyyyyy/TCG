# coding=utf-8
while True:
 a,b=input().split()
 flag=0
 if len(a)==len(b):
  flag=1
 s =a+a
 if b in s:
    flag = 1
 else:
    flag = 0

 if flag==1:
  print('Yes')
 if flag == 0:
  print('No')