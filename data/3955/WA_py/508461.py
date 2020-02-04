# coding=utf-8
while True:
    s=input()
    l=len(s)
    i=0
    a=0
    for i in range(0,l):
        if s[i]==' ':
            a=i
    if s[a-1]==s[a+1]:
        print('Yes')
    else:
        print('No')