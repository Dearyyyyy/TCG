# coding=utf-8
n=int(input())
d=2
p=1
s=0
for i in range (0,n):
    s=s+d/p
    t=d
    d=d+p
    p=t
print("%.2f" % s)