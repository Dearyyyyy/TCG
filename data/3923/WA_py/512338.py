# coding=utf-8
N = 1
strs_score = []
for i in range(N):
    strs_score.append(input())
for str_score in strs_score:
    for j in range(1,4):
        j_Y = str(j) + 'Y'
        j_N = str(j) + 'N'
        locals()['Y_' + str(j)] = str_score.count(j_Y)
        locals()['N_' + str(j)] = str_score.count(j_N)
    R = str_score.count('R')
    A = str_score.count('A')
    S = str_score.count('S')
    B = str_score.count('B')
    T = str_score.count('T')
    score = 1 * Y_1 + 2 * Y_2 + 3 * Y_3
    second = N_2 + N_3
    third = N_1
    efficient_value = (score + R + A + S + B) - second - third - T
    print(efficient_value)