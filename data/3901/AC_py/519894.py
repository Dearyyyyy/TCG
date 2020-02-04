# coding=utf-8
def function(x):
	return (x+1) * 2

N = int(input())
sum_peach = 1
for i in range(1, N):
	tmp = sum_peach
	sum_peach = function(tmp)
print(sum_peach)