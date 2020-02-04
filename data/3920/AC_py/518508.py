# coding=utf-8
s=int(input())
r=str(s)
p=0
for i in r:
    p=p+(int(i))**3
if p==s:
    print("YES")
else:
    print("NO")