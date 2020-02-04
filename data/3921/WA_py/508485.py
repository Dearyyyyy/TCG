# coding=utf-8
linum = input()
a = int(linum)
b= 0
for i in range(a):
  cod = str(input())
  b = len(cod)
  for j in range(b):
    if cod[j] == cod[b-1-j]:
      print('YES')
      break
    else:
      print('NO')
      break