# coding=utf-8
while(True):
    n1,n2 = input().split()
    n3 = "
    for i in range(len(n1)):
        n3 = n1[i:] + n1[i:]
        if n3 == n2 :
            print("YES")
            break
        else:
            print("NO")