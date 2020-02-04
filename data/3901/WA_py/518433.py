# coding=utf-8
n=int(input())
i=n
s=1
while i>0:
    if i%2==0:
        s=2*s
    else:
        s=2*(s+1)
    i=i-1
print(s)