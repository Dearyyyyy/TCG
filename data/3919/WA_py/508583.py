# coding=utf-8
def sanjiao(a,b,c):
	if a*a +b*b == c*c or a*a +c*c == b*b or c*c +b*b == a*a:
        print('ZJ')
    elif a == b and b ==c:
        print("DB")
    elif a==b or b == c or a ==c:
        print("DY")
    elif a+b>c and c+b>a and c+a>b:
        print('PT')
    else :
        print('ERROR')
while True:
	a,b,c = input().split()
	a,b,c = int(a),int(b),int(c)
	sanjiao(a,b,c)