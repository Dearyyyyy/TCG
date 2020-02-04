# coding=utf-8
n=int(input())
for i in range(n):
    string=input()
    Len=len(string)
    count=0
    flag=1
    while count<Len/2:
        if string[count]!=string[Len-count-1]:
            flag=0
            break
        count+=1
    if flag==1:
        print('YES')
    else:
        print('NO')