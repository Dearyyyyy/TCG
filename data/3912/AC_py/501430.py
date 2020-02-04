# coding=utf-8
flg = 0
a=int(input())
for i in range(2,a):
    if a % i == 0:
        print("not prime")
        flg = 1
        break
if(flg == 0):
    print("prime")