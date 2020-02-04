# coding=utf-8
n=int(input())
i=0
s=0
while i<n:
    str1=input()
    for m in range(len(str1)):
        if str1[m]==str1[len(str1)-m-1]:
            s=s
            
        else:
            s=s+1
    if s==0:
        print('YES')
    else:
        print('NO')
    i=i+1