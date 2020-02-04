# coding=utf-8
a=int(input())
for i in range(2,a+1):
    if(a%i==0):
        print('not prime')
        break
    else:
        print('prime')
        break