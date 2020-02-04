# coding=utf-8
while True:
    try:
        a=input()
        b="Y"
        i=0
        i=int(i)
        k=0
        k=int(k)
        while i<len(a)-1:
            c=a[i:i+2]
            if c[-1]=="Y":
                e=int(c[:c.index(b)])
                k=k+e
            i=i+2
        print(k)
    except:
        break