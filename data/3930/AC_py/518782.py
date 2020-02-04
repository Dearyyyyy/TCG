# coding=utf-8
n=int(input())
for i in range(n):
    list=[0]*7
    zhi=int(input())
    list[6]=zhi//100
    temp=zhi-list[6]*100
    list[5]=temp//50
    temp=temp-list[5]*50
    list[4]=temp//20
    temp=temp-list[4]*20
    list[3]=temp//10
    temp=temp-list[3]*10
    list[2]=temp//5
    temp=temp-list[2]*5
    list[1]=temp//2
    temp=temp-list[1]*2
    list[0]=temp
    for j in list:
        print(j,end=" ")
    print()