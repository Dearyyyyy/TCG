# coding=utf-8
f=1
while f==1:
    str=input()
    a=[0 for i in range(20)]
    for i in range(len(str)):
        if str[i]=='1' or str[i]=='2' or str[i]=='3':
            k=2*(ord(str[i])-48)-2
            i+=1
            if str[i]=='Y':a[k]+=1
            if str[i]=='N':a[k+1]+=1
        if str[i]=='R':a[6]+=1
        if str[i]=='A':a[7]+=1
        if str[i]=='S':a[8]+=1
        if str[i]=='B':a[9]+=1
        if str[i]=='T':a[10]+=1
    p=a[0]+2*a[2]+3*a[4]
    q=a[3]+a[5]
    c=p+a[6]+a[7]+a[8]+a[9]-q-a[1]-a[10]
    print(c)