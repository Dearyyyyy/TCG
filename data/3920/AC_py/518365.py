# coding=utf-8
def wgf(N:int):
	c = b //100
	d = (b - c*100)//10
	e = b %10
	if N == c**3+d**3+e**3:
		return 1
	else :
		return 0
while True:
	b = int(input())
	e = wgf(b)
	if e == 1:
		print("YES")
	else:
		print("NO")