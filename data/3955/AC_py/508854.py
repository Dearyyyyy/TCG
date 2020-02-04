# coding=utf-8
while True:
    A,B=list(input().split())
    if len(A)==len(B):
        if A in B*2 or B in A*2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')