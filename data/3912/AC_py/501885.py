# coding=utf-8
x=int(input())
s=0
for i in range(2,x):
    if x%i==0:
        s=s+1
    else:
        s=s
if s==0:
    print('prime')
else:
    print('not prime')