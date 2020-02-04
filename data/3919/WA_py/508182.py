# coding=utf-8
def sanjiao(a,b,c):
	if a == b and b ==c:
		print("DB")
	elif a==b or b == c or a ==c:
		print("DY")
	elif a*a +b*b == c*c or a*a +c*c == b*b or c*c +b*b == a*a:
		print('ZJ')
	elif a+b>c and c+b>a and c+a>b:
		print('PT')
	else :
		print('ERROR')
a ,b,c = input().split()
e ,d,f = input().split()
a,b,c = int(a),int(b),int(c)
e,d,f = int(e),int(d),int(f)
sanjiao(a,b,c)
sanjiao(e,d,f)