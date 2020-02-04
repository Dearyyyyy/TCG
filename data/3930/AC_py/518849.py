# coding=utf-8
t=int(input())
for i in range(t):
    n = int(input())
    relist=[0,0,0,0,0,0,0]
    restr = ''
     
    while n>0:
        if  n>=100:
            relist[6]=relist[6]+1
            n=n-100
        elif n>=50:
            relist[5]=relist[5]+1
            n=n-50
        elif n>= 20:
            relist[4]=relist[4]+1
            n=n-20
        elif n>=10:
            relist[3]=relist[3]+1
            n=n-10
        elif n>=5:
            relist[2]=relist[2]+1
            n=n-5
        elif n>=2:
            relist[1]=relist[1]+1
            n=n-2
        else:
            relist[0]=relist[0]+n
            n=n-n
    for i in relist:
        restr=restr+str(i)
        restr=restr+' '
    print(restr)