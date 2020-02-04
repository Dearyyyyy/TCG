# coding=utf-8
N = int(input())
str_list = []
for i in range(N):
    str_list.append(list(input()))
for i in range(N):
    str_list_r = str_list[i][:]
    str_list_r.reverse()
    if str_list[i] == str_list_r:
        print('YES')
    else:
        print('NO')