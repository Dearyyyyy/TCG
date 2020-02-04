# coding=utf-8
while True:
    n = int(input())
    sum = 1
    for _ in range(1,n): sum = (sum+1) * 2
    print(sum)