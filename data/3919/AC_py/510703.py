# coding=utf-8
def fun(a,b,c):
    if a== b ==c:
        print("DB")
    elif a+b<c or a+c<b or b+c<a:
        print("ERROR")
    elif a==b or a==c or b==c:
        print("DY")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("ZJ")
    else:
        print("PT")
while(1):
    x=[]
    x=list(map(int,input().split()))
    fun(x[0],x[1],x[2])