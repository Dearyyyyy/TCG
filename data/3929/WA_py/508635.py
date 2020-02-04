# coding=utf-8
while True:
    n = int(input())
    t = 0
    j = 0
    a = 0
    b = 0
    for i in range(n):
        time,s,m = input().split()
        timelist = time.split(":")
        timelist = [int(x) for x in timelist]
        shi = timelist[0]
        fen = timelist[1]
        if(n==1):
            if (m != 'AC'):
                t = t + 20
            else:
                a = a + (shi - 18)
                b = b + fen
        else:
            if(j!=n-1):
                if(m!='AC'):
                    t= t+20
                else:
                    a = a+(shi-18)
                    b = b+fen
            else:
                break
        j = j+1
    shi = a
    fen = b+t
    if(fen>=60):
        shi = shi+1
        fen = fen-60
        print('%02d:%02d'%(shi,fen))
    else:
        print('%02d:%02d'%(shi,fen))