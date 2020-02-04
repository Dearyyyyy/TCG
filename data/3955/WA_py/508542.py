# coding=utf-8
while True:
    a,b = input().split()
    if len(a) != len(b):
        print('No')
    else:
        i = len(a)
        while i > 0:
            if a[i-1] == b[0]:
                i -= 1
                while i>0:
                    if a[i-1] == b[i]:
                        i -= 1
                    else:
                        break
            else:
                break
        if i == 0:
            print('Yes')
        else:
            print('No')
        i = len(a)