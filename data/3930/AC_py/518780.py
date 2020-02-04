# coding=utf-8
def yuan(a):
    q=[100,50,20,10,5,2,1]
    p=[]
    for i in q:
        b=int(a/int(i))
        p.append(b)
        if a>=int(i):
            a=a%int(i)
    while p:
        print(p.pop(),end=' ')
    print('')
    return 

n=int(input())
for i in range(n):
    a=int(input())
    yuan(a)