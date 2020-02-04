# coding=utf-8
n = eval(input())
i = 1
flag = 1
while i*i < n:
   if(n%i == 0):
      flag = 0
      break
   i += 1
if flag == 1:
   print("prime")
else:
   print("not prime")