# coding=utf-8
a=int(input())
i=0
while i<a:
    s=input()
    s=str(s)
    k = ''.join(reversed(s))
    if k==s:
        print("YES")
    else:
        print("NO")
    i=i+1