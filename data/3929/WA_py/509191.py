# coding=utf-8
a=int(input())
while a!="":
    l=[]
    o=18*60
    s=0
    r=""
    for i in range(0,a):
        b,c,d=input().split()
        l.append(c)
        
        if d=="AC":
            if r==c:
                s=s
            else:
                r=c
                x,y=b.split(":")
                s=60*int(x)+int(y)-o+s
                f=l.count(c)
                s=s+(f-1)*20
    x=s//60
    y=s%60

    print("%02d:%02d"%(x,y))

        
            
        

          
    a=int(input())