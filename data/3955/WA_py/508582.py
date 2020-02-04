# coding=utf-8
while True:
    str=input()
    s1,s2=str.split(' ',1)
    str_double=s1+s1
    if s2 in str_double:
        print('Yes')
    else:
        print('No')