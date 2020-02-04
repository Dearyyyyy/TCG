# coding=utf-8
N = int(input())
a = int(N % 10)
b = int(N / 10 % 10)
c = int(N/ 100 % 10)
if a*a*a + b*b*b + c*c*c == N:
	print("YES")
else:
	print("NO")