# coding=utf-8
n=int(input())
flag=0
for i in range(2,n):
    if(n==1):
        flag=1
        print('not prime')
        break
    if(n%i==0):
        flag=1
        print('not prime')
        break
if(n==1):
    print('not prime')
else:
    if(flag==0):
        print('prime')