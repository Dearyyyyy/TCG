# coding=utf-8
summ=input()
summ=int(summ)
i=0
while i<summ:
    s = input()
    a = reversed(list(s))
    if list(a) == list(s):
        print('YES')
    else:
        print('NO')
    i=i+1