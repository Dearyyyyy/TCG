# coding=utf-8
import sys
def permutation(last_list, first_list=[]):
    if len(last_list) == 2:
        print(' '.join([str(number) for number in first_list + last_list]))
        print(' '.join([str(number) for number in first_list + list(reversed(last_list))]))
    else:
        for i in range(len(last_list)):
            first_list_sp = first_list[:]
            last_list_sp = last_list[:]
            first_list_sp.append(last_list_sp.pop(i))
            permutation(last_list_sp, first_list_sp)


for line in sys.stdin:
    N = int(line)
    if N == 0:
        break
    else:
        permutation(list(range(1, N + 1)))