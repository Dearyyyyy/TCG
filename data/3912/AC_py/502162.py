# coding=utf-8
number = int(input())
flag = 0
for factor in range(2,int(number/2)+1):
    if number % factor == 0:
        flag = 1
if flag == 0:
    print('prime')
else:
    print('not prime')