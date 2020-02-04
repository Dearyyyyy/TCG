# coding=utf-8
while True:
    a,b,c=input().split(' ')
    a=int(a);b=int(b);c=int(c)
    if a+b>c and b+c>a and a+c>b:
        if a==b and b==c and c==a:
            print('DB')
        elif a==b or b==c or c==a:
            print('DY')
        elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
            print('ZJ')
        else:
            print('PT')
    else:print('ERROR')