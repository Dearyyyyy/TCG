# coding=utf-8
while True:
    s = input()
    a = []
    for i in range(11):
        a[i] = 0
    for i in range(len(s)):
        if s[i]=='1' or s[i]=='2' or s[i]=='3':
            k = 2*(ord(s[i])-48)-2
            i+=1
            if s[i]=='Y': a[k]+=1
            if s[i]=='N': a[k+1]+=1
        if s[i]=='R': a[6]+= 1
        if s[i]=='A': a[7]+= 1
        if s[i]=='S': a[8]+= 1
        if s[i]=='B': a[9]+= 1
        if s[i]=='T': a[10]+= 1
    p=1*a[0]+2*a[2]+3*a[4]
    q=a[3]+a[5]
    c=p+a[6]+a[7]+a[8]+a[9]-q-a[1]-a[10]
    print(c)