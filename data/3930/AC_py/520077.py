# coding=utf-8
monetary_system = [100, 50, 20, 10, 5, 2, 1]
N = int(input())
for time in range(N):
    N = int(input())
    count_machine = []
    for i in range(len(monetary_system)):
        count_machine.append(str(int(N / monetary_system[i])))
        N -= int(count_machine[i]) * monetary_system[i]
    print(' '.join(reversed(count_machine)))