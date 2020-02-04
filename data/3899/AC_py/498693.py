# coding=utf-8
a=int(input())
b=2
c=1
d=0
for i in range (0,a):
    d=d+b/c
    t=b
    b=b+c
    c=t
print("%.2f" % d)