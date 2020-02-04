# coding=utf-8
while True:
    s=input()
    l=len(s)
    y,n,m,t=(0,0,0,0)
    for i in range(l):
        if s[i]=="1":
            if s[i+1]=="Y":
                y=y+1
            elif s[i+1]=="N":
                n=n+1
        elif s[i]=="2":
            if s[i+1]=="Y":
                y=y+2
            elif s[i+1]=="N":
                n=n+1
        elif s[i]=="3":
             if s[i+1]=="Y":
                y=y+3
             else:
                n=n+1
        elif s[i]=="A" or s[i]=="S" or s[i]=="R" or s[i]=="B":
                m=m+1
        elif s[i]=="T":
                t=t+1
    print(y+m-n-t)