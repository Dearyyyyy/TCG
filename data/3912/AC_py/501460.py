# coding=utf-8
def prime(number):
    n=int(number)
    for i in range(2,n):
        if n%i==0:
            
            
            
            print('not prime')
            break
    else:
        print('prime')
m=input()
prime(m)