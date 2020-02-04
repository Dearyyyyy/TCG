# coding=utf-8
n = input()
sum = 0
for i in n:
    sum += int(i)**3
if sum == int(n):
    print("YES")
else:
    print("NO")