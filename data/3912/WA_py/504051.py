# coding=utf-8
from math import sqrt
def is_prime():
    n = int(input())
    for i in range(n):
        for j in range(1,int(sqrt(n))):
            if i%j==0:
                break
            else:
                return True

# if n==1 or n==2:
#     print("prime")
if is_prime():
    print("prime")
else:
    print("not prime")