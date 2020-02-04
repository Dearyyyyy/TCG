# coding=utf-8
num = int(input())
sum = 0
n = len(str(num))
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
if num == sum:
   print(Yes)
else:
   print(No)