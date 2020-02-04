# coding=utf-8
while True:
	string1, string2 = map(str, input().split())
	m = len(string1)
	n = len(string2)
	if m != n:
		print("No")
		continue
	flag = False
	for i in range(m):
		tmp = ""
		tmp = tmp + string1[1:m] + string1[0]
		if tmp == string2:
			flag = True
			break
		string1 = tmp
	if flag:
		print("Yes")
	else:
		print("No")