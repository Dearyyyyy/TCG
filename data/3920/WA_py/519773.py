# coding=utf-8
import sys

for line in sys.stdin:
    number = int(line)
    number_list = list(line)
    cal = 0
    for i in range(3):
        cal += int(number_list[i]) ** 3
    if cal == number:
        print('YES')
    else:
        print('NO1')