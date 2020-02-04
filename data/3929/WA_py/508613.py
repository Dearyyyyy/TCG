# coding=utf-8


while True:
    n = eval(input())
    Sum = 0
    C=""
    timecal=[]
    for i in range(n):
        a,b,c=input().split()
        a,b,c=str(a),str(b),str(c)
        time = (int(a[0])*10+int(a[1]))*60+(int(a[3])*10+int(a[4]))
        if c.upper() == 'AC':
            Sum+=time-1080
            if(C.find(b)!=-1):
                Sum+=timecal[C.find(b)]*20

        elif c.upper() !="AC":
            if C.find(b)==-1:
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