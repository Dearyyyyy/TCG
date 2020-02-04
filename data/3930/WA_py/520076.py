# coding=utf-8
import sys

monetary_system = [100, 50, 20, 10, 5, 2, 1]
for line in sys.stdin:
    N = int(line)
    count_machine = []
    for i in range(len(monetary_system)):
        count_machine.append(str(int(N / monetary_system[i])))
        N -= int(count_machine[i]) * monetary_system[i]
    print(' '.join(reversed(count_machine)))