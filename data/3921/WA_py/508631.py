# coding=utf-8
n=int(input())
for i in range(n):
    s=input()
    a=len(s)
    for j in range(a):
        if s[j]==s[a-1-j] :
    
            b=0
        else :
            b=1
    if b==1 :
        print("NO")
    elif b==0:
        print("YES")