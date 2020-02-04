# coding=utf-8
def finda(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    num = 100*a+10*b+c
    if num == a*a*a+b*b*b+c*c*c:
       return "YES" 
    else:
       return "NO"
a,b,c = input()
print(finda(a,b,c))