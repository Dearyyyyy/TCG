# coding=utf-8
import sys

for line in sys.stdin:
    N = int(line)
    peach = 1
    for i in range(N-1):
        peach += 1
        peach *= 2
    print(peach)