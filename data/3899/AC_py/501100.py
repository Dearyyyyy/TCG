# coding=utf-8
n=int(input())
s=0
a=2
b=1
for i in range(n):
      s=a/b+s
      a,b=a+b,a
print('%.2f' % s)