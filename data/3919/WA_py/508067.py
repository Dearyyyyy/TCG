# coding=utf-8
i = 1
while i<=2:
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a+b<=c or a+c<=b or b+c<=a:
        print('ERROR')
    elif a==b or b==c or a==c:
        if a==b and b==c:
            print('DB')
        else:
            print('DY')
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+a*a==c*c:
        print('ZJ')
    else:
        print('PT')
    i +=1