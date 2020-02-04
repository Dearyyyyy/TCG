# coding=utf-8
a = int(input())
if a == 1:
    print("not prime")
elif a == 2:
    print("prime")
elif a>2:
    for i in (2,a//2+1):
        if a%i == 0:
            print("not prime")
            break;
    else:
        print("prime")
else:
    print("not prime")