# coding=utf-8
def decide_prime(a):
    if a<=1:
        flag = False
    else :
        flag = True
        for i in range(2,a):
            if a%i==0:
                flag = False
                break
    return flag

num = int(input())
if decide_prime(num):
    print("prime")
else:
    print("not prime")