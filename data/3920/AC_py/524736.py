# coding=utf-8
n = eval(input())
x = n
summ = 0
while x>=1:
   a = x % 10
   summ += (a**3)
   x = int(x/10)
if(summ == n):
   print("YES")
else:
   print("NO")