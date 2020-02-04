# coding=utf-8
ls = [0,0,0,0,0,0,0]

def fun(n):
    global ls
    while n != 0:
        if n >= 100:
            ls[6] += 1
            n -= 100
        elif n >= 50 and n < 100:
            ls[5] += 1
            n -= 50
        elif n >= 20 and n < 50:
            ls[4] += 1
            n -= 20
        elif n >= 10 and n < 20:
            ls[3] += 1
            n -= 10
        elif n >= 5 and n < 10:
            ls[2] += 1
            n -= 5
        elif n >= 2 and n < 5:
            ls[1] += 1
            n -= 2
        else:
            ls[0] = n;
            n = 0

n = eval(input())
for i in range(n):
    m = eval(input())
    fun(m)
    for j in range(7):
        print(ls[j],end=" ")
    print()
    ls = [0,0,0,0,0,0,0]