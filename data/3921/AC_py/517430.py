# coding=utf-8
while True:
    n=int(input())
    for _ in range(n):
        s=input()
        l=len(s)
        i=0
        j=l-1
        while i<= j:
            if s[i] !=s[j]:break
            i +=1;j -=1
        if i >= j:print('YES')
        else:print('NO')