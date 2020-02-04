# coding=utf-8
n = int(input())
p = 2#numerator
q = 1#denominator
l = []
s = 0
for i in range(1,n+1):
    a = p
    b = q
    s += (a/b)
    l.append('%s/%s'%(a,b)) 
    p = a+b
    q= a
print('%.2f'%s)