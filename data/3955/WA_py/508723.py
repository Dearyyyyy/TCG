# coding=utf-8
while True:
    str1,str2=input().split()
    if len(str1)==len(str2):
        str_double=str1+str1
        if str2 in str_double:
            print('Yes')
        else:
            print('No')
    else:
        break