# coding=utf-8
n=int(input())
 for i in range(n):
  a=input()
  b=a[::-1]

  if b==a:
     print('YES')
  else:
    print('NO')