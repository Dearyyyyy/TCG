# coding=utf-8
while True:
    a,b = map(str,input().split())
    c = a
    if len(a)==len(b):
        a = "a"+"c"
        for i in a:
            if i=="b":
                print("YES")
                break
    else:
        print("NO")