# coding=utf-8
n=int(input())
flag=0
if n==2:
    flag=1
for i in range(2,n):
    if n%i==0:
        flag=0
        break
    else:
        flag+=1
if flag==0:
    print('not prime')
else:
    print('prime')