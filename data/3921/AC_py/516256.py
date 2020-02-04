# coding=utf-8
n = int(input())
while n > 0:
	string = input()
	#print(type(string))
	i = len(string)-1
	k = int(len(string) / 2)
	flag = 0
	for j in range(k):
		if string[j] != string[i]:
			flag = 1
			break
		i -= 1
	if flag == 1:
		print("NO")
	else:
		print("YES")