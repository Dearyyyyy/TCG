# coding=utf-8
for i in range(3):
    triangle = input().split()
    
    a,b,c = sorted(triangle)
    a = int(a)
    b = int(b)
    c = int(c)
    
    if c > a + b:
        print('ERROR')
    elif a == b == c:
        print('DB')
    elif a == b or b == c:
        print('DY')
    elif c*c == a*a + b*b:
        print('ZJ')
    else:
        print('PT')