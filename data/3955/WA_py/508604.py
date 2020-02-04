# coding=utf-8
while True:
    a,b=input().split(" ")
    a=str(a)
    b=str(b)
    k = ''.join(reversed(a))
    for j in k:
        c=j
        break
    for p in b:
        d=p
        break
    if c==d:
        print("YES")
    else:
        print("NO")