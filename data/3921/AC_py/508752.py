# coding=utf-8
b=int(input())
while True:
  a = input()
  flag=0
  x=len(a)
  for i in range(0, x):
    if a[i]!=a[x-1-i]:
     flag=1
  if flag==0:
    print('YES')
  else:
     print('NO')