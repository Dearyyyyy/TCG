# coding=utf-8


while True:
    n = eval(input())
    Sum = 0
    C=""
    for i in range(n):
        a,b,c=input().split()
        a,b,c=str(a),str(b),str(c)
        time = (int(a[0])*10+int(a[1]))*60+(int(a[3])*10+int(a[4]))
        if c.upper() == 'AC' and b not in C :
            Sum+=time-1080
            C+=b
        elif c.upper() =="WA" and b not in C:
            Sum+=20
    s=""
    s+=str(Sum//60//10)
    s+=str(Sum//60%10)
    s+=':'
    s+=str(Sum%60//10)
    s+=str(Sum%60%10)
    print(s)