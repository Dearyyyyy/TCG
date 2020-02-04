# coding=utf-8
def is_rotation(str1, str2):
    if str1 == "" or str2 == "" or len(str1) != len(str2):
        return False
    str_double = str1 + str1
    if str2 in str_double:
        return True
    else:
        return False
while True:
    s=[str(i) for i in input().split()]
    s1=[]
    s2=[]
    s1=[s[0]]
    s2=[s[1]]
    len1=len(s1[0])
    len2=len(s2[0])
    if is_rotation(s1[0], s2[0])==True:
        print('Yes')
    else:
        print('No')