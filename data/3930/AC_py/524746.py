# coding=utf-8
import math
money = [1,2,5,10,20,50,100]
money.reverse()
T = eval(input())
while T > 0:
   T -= 1
   n = eval(input())
   i = 0
   l = []
   while i < 7:
      a = math.floor(n / money[i])
      n %= money[i]
      i += 1
      l.append(a)
   l.reverse()
   for item in l:
      print(item,end = " ")
   print()