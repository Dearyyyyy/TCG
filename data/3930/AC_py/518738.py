# coding=utf-8
i = int(input())
while i >0:
    n = input()
    n = int(n)
    x1,x2,x3,x4,x5,x6,x7=0,0,0,0,0,0,0
    x7 = n // 100
    n = n-100*x7
    x6 = n // 50
    n = n-50*x6
    x5 = n //20
    n = n-20*x5
    x4 = n //10
    n = n-10*x4
    x3 = n //5
    n = n-5*x3
    x2 = n //2
    x1 = n-2*x2
    i -=1
    print(x1,x2,x3,x4,x5,x6,x7)