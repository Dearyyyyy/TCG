# coding=utf-8
while True:
    a,b = input().split()
    i = 0
    while i<len(a):
        if a[i] == b[len(a)-i-1]:
            i +=1
        else:
            break
    if i ==len(a):
        print('Yes')
    else:
        print('No')
    i = 0