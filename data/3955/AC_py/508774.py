# coding=utf-8
while True:
    a,b = input().split()
    c = a + a
    if b in c and len(a) == len(b):
        print('Yes')
    else:
        print('No')