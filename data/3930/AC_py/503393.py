# coding=utf-8
n = int(input())
while n > 0:
    a = [1, 2, 5, 10, 20, 50, 100]
    c = [0 for _ in range(len(a))]
    t = int(input())
    i = 6
    while t != 0:
        c[i] = int(t/a[i])
        t = int(t % a[i])
        i -= 1
    for i in c: print(i,end=' ')
    print()
    n -= 1