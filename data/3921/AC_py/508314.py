# coding=utf-8
a = int(input())
for i in range(a):
 n =  input()
 rn = list(reversed(n))
 if list(n) == rn:
      print("YES")
 else:
      print("NO")