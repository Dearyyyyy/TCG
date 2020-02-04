# coding=utf-8
n=int(input())
a=2
b=1
s=0
for i in range(1,n+1):
    s=s+(a/b)
    k=a
    a=b+k
    b=k
print("{:.2f}".format(s))