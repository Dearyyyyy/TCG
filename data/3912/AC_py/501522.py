# coding=utf-8
while True:
    n=int(input())
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    if n==i+1:
        print("prime")