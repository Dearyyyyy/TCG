# coding=utf-8
def find(now,base):
    k=0
    while True:
        if k*base>now:
            break
        else:
            k=k+1
    return k-1

a=int(input())
for i in range(a):
    num=int(input())
    res=[]
    string=""

    num1=find(num,100)
    num=num%100
    res.append(num1)

    num2 = find(num, 50)
    num=num%50
    res.append(num2)

    num3 = find(num, 20)
    num = num % 20
    res.append(num3)

    num4 = find(num, 10)
    num = num % 10
    res.append(num4)

    num5 = find(num, 5)
    num = num % 5
    res.append(num5)

    num6 = find(num, 2)
    num = num % 2
    res.append(num6)

    num7 = find(num, 1)
    res.append(num7)
    res.reverse()
    for j in res:
        print(j)