# coding=utf-8
def sanjiao(a,b):
	if b == 0:
		print('error')
	elif a/b-a//b>=1/2:
		print((a//b)+1)
	else:
		print(a//b)		
while True:
	a ,b = input().split()
	a,b= int(a),int(b)
	sanjiao(a,b)