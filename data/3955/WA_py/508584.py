# coding=utf-8
while True:
    str=input()
    s1,s2=str.split(' ',1)
    s_double=s1+s1
    if s2 in s_double:
        print('Yes')
    else:
        print('No')