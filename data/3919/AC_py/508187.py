# coding=utf-8
while True:
    try:
        a,b,c=input().split()
        a=int(a)
        b=int(b)
        c=int(c)
        if a+c<b or a+b<c or b+c<a :
            print("ERROR")
        elif a==b or a==c or b==c:
            if a==b==c:
                print("DB")
            else:
                print("DY")
        elif (a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a) :
            print("ZJ")
        else:
            print("PT")
            
    except:
        break