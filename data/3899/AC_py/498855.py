# coding=utf-8
n = int(input(''))
sum_1 = 0
a =[2,3]
b =[1,2]
d,f= 0,0
for i in range(2,n) :
	d = a[i-1]+a[i-2]
	a.append(d)
for i in range(2,n):
	f = b[i-1]+b[i-2]
	b.append(f)
for i in range(0,n):
	c = a[i]/b[i]
	sum_1 = sum_1 +c
print("%.2f" %sum_1)