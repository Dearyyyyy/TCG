# coding=utf-8
n = int(input())
for i in range(n):
    num = int(input())
    if num>=100:
        a = num//100
        num = num - 100 * a
    else:
        a = 0
    if num>=50:
        b = num//50
        num = num - 50
    else:
        b = 0
    if num>=20:
        c = num//20
        num = num - 20
    else:
        c = 0
    if num>=10:
        d = num//10
        num = num - 10 * d
    else:
        d = 0
    if num>=5:
        e = num//5
        num = num - 5 * e
    else:
        e = 0
    if num>=2:
        f = num//2
        num = num - 2 * f
    else:
        f = 0
    if num>=1:
        g = num//1
        num = num - 1 * g
    else:
        g = 0
    print(g,f,e,d,c,b,a)