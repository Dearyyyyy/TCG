# coding=utf-8
linum = input()
a = int(linum)
b= 0
for i in range(a):
  cod = str(input())
  b = len(cod)
  for i in range(b):
    if cod[i] == cod[b-1-i]:
      print('YES')
      break
    else:
      print('NO')
      break