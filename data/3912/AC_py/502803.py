# coding=utf-8
x=int(input())
e=0
for i in range(1,x):
    if(x%i==0):
        e=e+1
if(e==1):
    print('prime')
else:
    print('not prime')