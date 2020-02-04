# coding=utf-8
a=2
b=1
sum=0
for i in range(10):
    sum=a/b+sum
    a,b=(a+b),a
print('{0:.2f}'.format(sum))