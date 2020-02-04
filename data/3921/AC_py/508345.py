# coding=utf-8
def is_palindromic4(num):
    return num == num[::-1]
g = int(input(''))
i = 0
h = []
while i < g:
	c = list(input(''))
	d = is_palindromic4(c)
	if d == True:
		h.append(1)
	else:
		h.append(0)
	i += 1
for j in h:
	if j == 1:
		print('YES')
	else:
		print('NO')