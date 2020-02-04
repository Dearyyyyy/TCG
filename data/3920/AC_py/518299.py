# coding=utf-8
i=int(input())
a=int(i%10)
c=int(i/100)
b=int((i%100-a)/10)

if(a**3+b**3+c**3==i):
    print("YES")
else:
    print("NO")