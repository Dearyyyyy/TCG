# coding=utf-8
num = int(input())
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("not prime")
                break
        else:
            print("prime")
    else:
        print("not prime")
is_prime(num)