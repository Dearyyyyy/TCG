def fb(n):
    a=1
    b=1
    c=0
    d=1
    summ=0
    while n:
       summ+=float(a+b)/(c+d)
       a,b=b,a+b
       c,d=d,c+d
       n-=1
    return summ
print("%.2f" %fb(10))