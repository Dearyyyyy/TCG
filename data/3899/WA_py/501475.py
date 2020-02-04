# coding=utf-8
N = int( input())
a = 2
b = 1
sn = 0
for i in range (N):
    sn= sn + a/b
    a = a+b
    b = a
print ('%.2f'%sn)