# coding=utf-8
n=eval(input())
for i in range(n):
    m=input()
    count=0
    if len(m)%2==0:
        for j in range(int(len(m)/2)):
            if m[j]!=m[len(m)-1-j]:
                count=1
    else :
        for j in range(int((len(m)-1)/2)):
            if m[j]!=m[len(m)-1-j]:
                count=1
    if count==1:
        print("NO")
    else:
        print("YES")