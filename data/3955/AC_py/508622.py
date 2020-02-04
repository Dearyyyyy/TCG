# coding=utf-8
while True :
    fl=0
    str1,str2=input().split()
    list_str1=list(str1)
    list_str2=list(str2)
    for i in range(len(str1)):
        if list_str1==list_str2:
            fl=1
            break
        else:
            mn=list_str1.pop(0)
            list_str1.append(mn)
    if fl==1:
        print('Yes')
    else:
        print('No')