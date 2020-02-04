# coding=utf-8
m = int(input())
n = int(m/2)
flag = 0
for i in range(2, n+1):
	if m % i == 0:
		flag = 1
		break
if flag == 0:
	print("prime")
else:
	print("not prime")