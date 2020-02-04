# coding=utf-8
n = int(input())
 
c = 2
d = 1
l = []
s = 0
 
for i in range(1,n+1):
    a = c
    b = d
    
    s += (a/b)
    l.append('%s/%s'%(a,b))
    
    c = a+b
    d = a

print('%.2f'%s)