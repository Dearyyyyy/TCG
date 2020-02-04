# coding=utf-8
list_number = [1., 2., 3., 5., 8., 13.]
for i in range(6, 1000):
	list_number.append(list_number[i-1] + list_number[i-2])
N = int(input())
sum = 0.0
for i in range(N):
	sum += list_number[i + 1] / list_number[i]
print("{:.2f}".format(sum))