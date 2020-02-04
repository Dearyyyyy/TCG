# coding=utf-8
while 1:
    s1,s2=str(input()).split()
    for i in range(len(s2)):
        c=s1[i:]+s1[:i]
        if c==s2:
            print('YES')
            break
    else:
        print('NO')