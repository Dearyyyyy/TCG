# coding=utf-8
def prime(a):
    for i in range(2,a):
        if a%i==0:
            print('not prime')
            break
        if i==a-1:
            print('prime')
            break;
    return
n=int(input())
prime(n)