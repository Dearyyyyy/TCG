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
                t = 0
                a = 0
                b = 0
            else:
                a = a + (shi - 18)
                b = b + fen
        else:
            if(m!='AC'):
                t = t+1
                j = j+1
                c = s
            else:
                if(s==c):
                    a = a+(shi-18)
                    b = b+fen+t*20
                else:
                    a = a+(shi-18)
                    b = b+fen
    if(j==n):
        shi = 0
        fen = 0
        print('%02d:%02d'%(shi,fen))
    else:
        shi = a
        fen = b
        if(fen>=60):
            shi = shi+1
            fen = fen-60
            print('%02d:%02d'%(shi,fen))
        else:
            print('%02d:%02d'%(shi,fen))