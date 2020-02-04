# coding=utf-8
import sys
while True:
    a,b,c=map(int,input().split())
    if(a+b>c and a+c>b and b+c>a):
        if a==b and b==c:
            print("DB")
        else:
            if a==b or b==c:
                print('DY')
            else:
                if b*b+c*c==a*a or a*a+c*c==b*b or a*a+b*b==c*c:
                    print('ZJ')
                else:
                    print("PT")
    else:
        print("ERROR")