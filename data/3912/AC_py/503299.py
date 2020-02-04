# coding=utf-8
a=[]
def isprime(n):
    for i in range(2,n*n):
        if i not in a:
            j=i*i
            while j<n*n:
                a.append(j)
                j+=i


n=int(input())
isprime(n)
if n in a:
    print("not prime")
else: 
    print("prime")