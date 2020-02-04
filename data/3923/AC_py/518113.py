# coding=utf-8
while True:
    s=input()
    a=[0 for i in range(11)]
    for i in range(len(s)):
        if s[i]=='1' or s[i]=='2' or s[i]=='3':
            m=2*(ord(s[i])-48)-2
            i+=1
            if s[i]=='Y':
                a[m]+=1
            if s[i]=='N':
                a[m+1]+=1
        if s[i]=='R':
            a[6]+=1
        if s[i]=='A':
            a[7]+=1
        if s[i]=='S':
            a[8]+=1
        if s[i]=='B':
            a[9]+=1
        if s[i]=='T':
            a[10]+=1
    x=1*a[0]+2*a[2]+3*a[4]
    y=a[3]+a[5]
    c=x+a[6]+a[7]+a[8]+a[9]-y-a[1]-a[10]
    print(c)