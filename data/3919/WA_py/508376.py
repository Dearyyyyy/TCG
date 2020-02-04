# coding=utf-8
while True:
    a,b,c=input().split()
    a,b,c=int(a),int(b),int(c)
    if a+b<=c or a+c<=b or b+c<=a:
        print("ERROR")
    elif a==b and b==c:
        print("db")
    elif a==b or a==c or b==c:
        print("dy")
    elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
        print("zj")
    else:
        print("pt")