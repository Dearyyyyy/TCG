# coding=utf-8
n = int(input())
for i in range(n):
    m = int(input())
    res_list = [0,0,0,0,0,0,0]
    res_str = ''
    while m > 0:
        if m >= 100:
            res_list[6] += 1
            m -= 100
        elif m >= 50:
            res_list[5] += 1
            m -= 50
        elif m >= 20:
            res_list[4] += 1
            m -=20
        elif m >= 10:
            res_list[3] += 1
            m -= 10
        elif m >= 5:
            res_list[2] += 1
            m -= 5
        elif m >= 2:
            res_list[1] += 1
            m -= 2
        else:
            res_list[0] += m
            m -= m
    for i in res_list:
        res_str += str(i)
        res_str += ' '
    print(res_str)