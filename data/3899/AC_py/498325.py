# coding=utf-8
r =int(input())
fenzi = 2  
fenmu = 1  
l = []
s = 0

for i in range(1, r + 1):
    a = fenzi
    b = fenmu

    s += (a / b)
    l.append('%s/%s' % (a, b))

    fenzi = a + b
    fenmu = a
print('%.2f' % s)