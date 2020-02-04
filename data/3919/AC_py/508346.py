# coding=utf-8
while (True) :
    a,b,c=input().split()
    a,b,c=int(a),int(b),int(c)
    if  a+b>c and a+c>b and b+c>a :
        if  a==b and b==c :
            print("DB")
        elif a==b or b==c :
            print("DY")
        elif (a*a+b*b)==c*c or (a*a+c*c)==(c*c) or (b*b+c*c)==a*a :
            print("ZJ")
        else  :
            print("PT")
    else :
        print("ERROR")