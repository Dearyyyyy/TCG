# coding=utf-8
def sanjiao(a,b):
	if b == 0:
		print('error')
	elif a/b>=1:
		print(a/b)
	elif a/b > 2/5 and a/b <1:
		print(1)
	else:
		print(0)		
a ,b = input().split()
c ,d = input().split()
e,f =input().split()
a,b= int(a),int(b)
c,d = int(c),int(d)
e,f = int(e),int(f)
sanjiao(a,b)
sanjiao(c,d)
sanjiao(e,f)