# coding=utf-8
n=int(input())
for i in range(n):
    s=input()
    a=len(s)
    for j in range(a):
        if s[j]==s[a-1-j] :
            j=j+1
            b=0
        else :
            b=1
    if(i!=n-1) :
        if b==1 :
            print("NO")
        elif b==0:
            print("YES")
    if(i==n-1) :
        if b==1 :
            print("NO",end="")
        elif b==0:
            print("YES",end="")