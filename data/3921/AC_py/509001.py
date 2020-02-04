# coding=utf-8
for _ in range(int(input())):
    a = [str(y) for y in input()]
    b=a[::-1]
    if a==b:
        print("YES")
    else:
        print("NO")