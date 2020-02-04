# coding=utf-8
while True:
    a,b,c=input().split()
    a,b,c=int(a),int(b),int(c)
    if a+b>c and b+c>a and a+c>b:
        if a==b==c:
            g="DB"
        elif a==b or b==c or c==a:
            g="DY"
        elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
            g="ZJ"
        else:
            g="PT"
    else:
        g="ERROR"
    print(g)