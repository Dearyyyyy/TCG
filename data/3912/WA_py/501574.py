# coding=utf-8
a = int(input())
if a == 1:
    print("not prime")
elif a>1:
    for i in (2,a):
        if a%i == 0:
            print("prime")
            break;
    else:
        print("not prime")