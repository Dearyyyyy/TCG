# coding=utf-8
while True:
    a,b = input().split()
    c = a + a
    if b in c:
        print('Yes')
    else:
        print('No')