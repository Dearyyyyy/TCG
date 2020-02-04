# coding=utf-8
a=int(input())
i=0
d=2
c=1
sn=0
while i<a:
    sn=d/c+sn
    s=d
    d=c+d
    c=s
    i=i+1
print("%.2f" % sn)