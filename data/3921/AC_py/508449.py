# coding=utf-8
n=int(input())
for i in range(n):
  s=input()
  if s=="".join(reversed(s)):
      print("YES")
  else:
      print("NO")