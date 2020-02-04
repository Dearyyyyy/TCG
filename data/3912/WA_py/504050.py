# coding=utf-8
# def is_prime(n):
#     for i in range(n):
#         for j in range(2,n):
#             if i%j==0:
#                 break
#             else:
#                 return True
from math import sqrt
def is_prime(n):
    for i in range(n):
        for j in range(1,int(sqrt(n))):
            if i%j==0:
                break
        else:
            return True
n = int(input())
# if n==1 or n==2:
#     print("prime")
if is_prime(n):
    print("prime")
else:
    print("not prime")