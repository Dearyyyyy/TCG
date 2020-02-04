# coding=utf-8
k=1
p=1
while True
    a,b=input().split()
    if len(a)!=len(b):
        print("No")
        p=0
    elif len(a)==0 and len(b)==0:
        print('Yes')
        p=0
    elif len(a)==1 and len(b)==1 and a==b:
        print('Yes')
        p=0
    if p==1:
        List=[]
        List.append(a)
        for i in range(1,len(a)-1):
            List.append(a[i]+a[i+1]+a[:i])
        List.append(a[-1]+a[:len(a)-1])
        if b in List:
            print('Yes')
        else:
            print('No')