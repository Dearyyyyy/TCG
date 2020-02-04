# coding=utf-8
def judgePrime(n):
	if n <=1: 
		return False
	i = 2
	while i*i <= n:
		if n%i == 0 : 
			return False
		i += 1
	return True
b = int(input(""))
if judgePrime(b):
	print('prime')
else:
	print('not prime')