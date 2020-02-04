# coding=utf-8
n = int(input())
a = int(n/100)
b = int((n-a*100)/10)
c = n%10
if a**3+b**3+c**3 == n:
    print("YES")
else :
    print("NO")