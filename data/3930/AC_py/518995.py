# coding=utf-8
n = int(input())
o = 0
while o < n:
	i = 0
	c = [1,2,5,10,20,50,100]
	d = [0,0,0,0,0,0,0]
	b = int(input(''))
	while b>0:
		count = 0
		for i in c:
			if b<i:
				break
			else :
				count += 1
		b = b - c[count-1]
		d[count-1] += 1
	for i in d :
		print(i,end = " ")
	print("")
	o += 1