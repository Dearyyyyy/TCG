# coding=utf-8
daffodil = int(input())
if daffodil == pow(daffodil // 100 , 3) + pow(daffodil % 10 , 3) + pow(daffodil // 10 % 10, 3):
    print("YES")
else:
    print("NO")