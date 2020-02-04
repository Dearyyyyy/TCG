# coding=utf-8
n=int(input())
for i in range(n):
    str1=input()
    l=len(str1)
    i=0
    newstr=list(str1)
    while newstr[i] in newstr[l-1-i]:
        i+=1
        if i==l:
            break
    if i==l :
        print('YES')
    else :
        print('NO')