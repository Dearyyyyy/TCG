# coding=utf-8
a=int(input())
s=0
for i in range(2,a):
    if a%i==0:
        s=s+1
    else:
        s=s
if s==0:
    print('prime')
else:
    print('not prime')