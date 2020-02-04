# coding=utf-8
# this is a new learning program

while True:
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if a + b <= c or abs(a - b) >= c:
        print('ERROR')
    elif a == b and b == c:
        print('DB')
    elif a == b or b == c or a == c:
        print('DY')
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('ZJ')
    else:
        print('PT')