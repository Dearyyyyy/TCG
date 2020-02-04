# coding=utf-8
n = int(input())
fz = 2
fm = 1
l = []
s = 0
for i in range(1,n+1):
    a = fz
    b = fm
    s += (a/b)
    l.append('%s/%s'%(a,b))
    fz = a+b
    fm = a
print('%.2f'%s)