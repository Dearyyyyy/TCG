# coding=utf-8
import sys

for str_score in sys.stdin:
    str_score = input()
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
    second = Y_2 + N_2 + Y_3 + N_3 - Y_2 - Y_3
    third = Y_1 + N_1 - Y_1
    efficient_value = (score + R + A + S + B) - second - third - T
    print(efficient_value)