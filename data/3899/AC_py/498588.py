# coding=utf-8
N = input()
N = int(N)
i = 1
a = 2
b = 1
sum = 0.0
while i<=N:
    sum=sum+a/b
    temp=a
    a=b+temp
    b=temp
    i=i+1
print('%.2f'% sum)