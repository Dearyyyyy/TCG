# coding=utf-8
def xuanzhuan(c,d):
		i = 0
		b = c
		while i<len(c)-1:
			b = b + b[0]
			b = b.lstrip(b[0])
			if d == b:
				return 1
			i += 1
		print('NO')
while True:
	a,b = input().split()
	c = xuanzhuan(a,b)
	if c == 1:
		print('YES')