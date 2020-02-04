# coding=utf-8
c = int(input())
i = 0
j = 0
g = []
while i<c:
	s = input('')
	d = reversed(s)
	if s == d:
		g.append('1')
	else :
		g.append('0')
	i+=1
for j in g:
	if j == 1:
		print("YES")
	else :
		print("NO")