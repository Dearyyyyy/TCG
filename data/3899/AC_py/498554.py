# coding=utf-8

n = int(input())
 
fenzi = 2#分子
fenmu = 1#分母
l = []
s = 0
 
for i in range(1,n+1):
    a = fenzi
    b = fenmu
    
    s += (a/b)
    l.append('%s/%s'%(a,b))
    
    fenzi = a+b
    fenmu = a

print('%.2f'%s)