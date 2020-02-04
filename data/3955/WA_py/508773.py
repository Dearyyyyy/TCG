# coding=utf-8
while True:
    str1,str2=input().split()
    c=''
    for i in range(lan(a)):
        c=str1[i:]+str1[:i]
        if c==str2:
            print('Yes')
            break
    else:
        print('No')