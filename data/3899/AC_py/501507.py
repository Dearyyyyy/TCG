# coding=utf-8
N = int( input())
a = 2
b = 1
sn = 0
for i in range (N):
    sn= float(a/b) + sn
    a,b = a+b, a
print ('%.2f'%sn)