# coding=utf-8
num = int(input())
ge_num = num % 10
bai_num = num // 100
shi_num = (num - bai_num * 100 - ge_num) // 10
if ge_num ** 3 + shi_num ** 3 + bai_num ** 3 == num:
    print('YES')
else:
    print('NO')