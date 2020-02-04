# coding=utf-8
# this is a new learning program

while True:
    a, b = input().split()
    a, b = str(a), str(b)
    step = b.find(a[0])
    if a.__len__() != b.__len__():
        print('No')
        continue
    for i in a:
        if b[(a.find(i) + step) % a.__len__()] != i and b.find(i) == -1:
            print('No')
            break
    else:
        print('Yes')