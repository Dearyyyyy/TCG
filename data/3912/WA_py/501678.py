# coding=utf-8
n = int(input(""))

if n < 2:

    print("not prime")

else:

    for x in range(2,n):  

        if n % x == 0:  

            print("not prime")

        else:

            print("prime")