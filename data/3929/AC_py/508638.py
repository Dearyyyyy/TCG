# coding=utf-8


while True:
    n = eval(input())
    Sum = 0
    C=""
    OK = ""
    timecal = []
    for i in range(n):
        a,b,c=input().split()
        a,b,c=str(a),str(b),str(c)
        time = (int(a[0])*10+int(a[1]))*60+(int(a[3])*10+int(a[4]))
        if c.upper() == 'AC'and b not in OK:
            Sum+=time-1080
            if b in C:
                Sum+=timecal[C.find(b)]*20
            OK += b
        elif c.upper() !="AC":
            if b not in C:
                C+=b
                timecal.append(1)
            else:
                timecal[C.find(b)] +=1

    s=""
    s+=str(Sum//60//10)
    s+=str(Sum//60%10)
    s+=':'
    s+=str(Sum%60//10)
    s+=str(Sum%60%10)
    print(s)