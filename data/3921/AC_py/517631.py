# coding=utf-8
f=1
while f==1:
    n=int(input())
    for m in range(n):
        s=input()
        l=len(s)
        i=0
        j=l-1
        while i<=j:
            if s[i]!=s[j]:break
            i+=1; j-=1
        if i>=j:print('YES')
        else:print('NO')