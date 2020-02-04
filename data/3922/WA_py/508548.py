# coding=utf-8
def sanjiao(a,b):
	if b == 0:
		print('error')
	elif a/b>1:
		if a/b-a//b>=1/2:
			print(a//b+1)
		else:
			print(a//b)
	elif a/b > 2/5 and a/b <1:
		print(1)
	else:
		print(0)		
while True:
	a ,b = input().split()
	a,b= int(a),int(b)
	sanjiao(a,b)