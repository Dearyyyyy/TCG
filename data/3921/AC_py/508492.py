# coding=utf-8
linum = input()
a = int(linum)
b= 0
for i in range(a):
  cod = str(input())
  cod1 = cod[::-1]
  if cod1 == cod:
      print('YES')
  else:
      print('NO')