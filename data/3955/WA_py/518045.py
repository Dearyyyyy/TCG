# coding=utf-8
k=1
while True
    a,b=input().split()
    if len(a)!=len(b):
        print("No")
    elif len(a)==0 and len(b)==0:
        print('Yes')
    elif len(a)==1 and len(b)==1 and a==b:
        print('Yes')
    else:
        for j in range(len(a)):
            for i in range(len(a)):
                if k==1:
                    f=a[i]
                    k--
                a[i]=a[i+1]
                if i==len(a)-2:
                    a[len(a)-1]=f;k++;break
            if a==b:
                print('Yes');q=1;break
        if q!==1:
            print('No')