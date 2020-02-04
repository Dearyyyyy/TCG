# coding=utf-8
r1 = input().split()
r2 = input().split()
r3 = input().split()
rr = [r1,r2,r3]
for i in range(0,3):
	m=""
	for r in rr:
		m = m+r[i]+" "
	print(m)