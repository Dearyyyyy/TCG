# coding=utf-8
while True:
    a, b = input().split()
    a, b = int(a), int(b)
    if b == 0:
        print('error')
    else:
        c = int(a*1.0/b + 0.5)
        print(c)