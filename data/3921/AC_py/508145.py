# coding=utf-8
n = input()
n = int(n)
i = 0
j = 0
while i< n:
    str1 = input()
    while j<len(str1):
        if str1[j] == str1[len(str1)-j-1] :
            j +=1
        else:
            break
    if j == len(str1):
        print('YES')
    else:
        print('NO')
    j = 0
    i +=1