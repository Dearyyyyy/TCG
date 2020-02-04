# coding=utf-8


while True:
    n = eval(input())
    Sum = 0
    for i in range(n):
        a,b,c=input().split()
        a,b,c=str(a),str(b),str(c)
        time = (int(a[0])*10+int(a[1]))*60+(int(a[3])*10+int(a[4]))
        if c.upper() == 'AC':
            Sum+=time-1080
        elif c.upper() =="WA":
            Sum+=20
    s=""
    s+=str(Sum//60//10)
    s+=str(Sum//60%10)
    s+=':'
    s+=str(Sum%60//10)
    s+=str(Sum%60%10)
    print(s)