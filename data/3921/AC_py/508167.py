# coding=utf-8
a=int(input())
i=0
while i<a:
    s = input()
    Len = len(s)
    count = 0
    flag = 1
    while count < Len//2:
        if s[count] != s[Len-count-1]:
            flag = 0
            break
        count += 1
    if flag == 1:
        print('YES')
    else:
        print('NO')
    i+=1