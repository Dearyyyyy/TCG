# coding=utf-8
while True:
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if a+b > c and a+c > b and b+c > a:
        if b == a and a == c:
            print('DB')
        elif a == b or a == c or b == c:
            print('DY')
        elif a**2+b**2 == c**2 or a**2+c**2 == b**2 or b**2+c**2 == a**2:
            print('ZJ')
        else:
            print('PT')
    else:
        print('ERROR')