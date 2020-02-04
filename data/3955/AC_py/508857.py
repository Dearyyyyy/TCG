# coding=utf-8
while True:
    a,b=list(input().split())
    if len(a)==len(b):
        if a in b*2 or b in a*2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')