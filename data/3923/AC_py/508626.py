# coding=utf-8
while(True):
    a=input()
    sum1=0
    k=0
    m=0
    n=0
    o=0
    p=0
    q=0
    for i in a:
        if(i=="Y"):
            sum1+=ord(a[k-1])-48
            if(a[k-1]=="1"):
                n+=1
                p+=1
            else:
                m+=1
                o+=1
        if(i=="R" or i=="A" or i=="S" or i=="B"):
            sum1+=1
        if(i=="N"):
            if(a[k-1]=="1"):
                n+=1
            else:
                m+=1
        if(i=="T"):
            q+=1
        k+=1
    print(sum1-(n-p)-(m-o)-q)