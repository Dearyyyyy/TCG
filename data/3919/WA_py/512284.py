# coding=utf-8
triangles = []
for i in range(3):
    triangles.append(input().split())
    
for triangle in triangles:
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