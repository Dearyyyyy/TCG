# coding=utf-8
while True:
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if a+b>c and a+c>b and b+c>a:
        if a==b and a==c:
            print('DB')
        elif a==b and b!=c or a==c and a!=b or b==c and b!=a:
            print('DY')
        elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
            print('ZJ')
        else:
            print('PT')
    else:
        print('ERROR')