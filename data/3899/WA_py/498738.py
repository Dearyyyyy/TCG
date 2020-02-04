# coding=utf-8
s=int(input())
flag=1
n=0
for i in range (2,s):
    for j in range (2, s):
        if i==j:
            continue
        if i%j==0:
            flage=0
            break
    if flag==1:
        n += 1
    flag=1
print ('%d'%n)