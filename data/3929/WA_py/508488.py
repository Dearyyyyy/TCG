# coding=utf-8
while True:
    n = int(input())
    count = 0
    problem = []
    penalty = ''
    for i in range(n):
        time, problem1, status = input().split()
        h = time[:2]; m = time[3:]
        h = int(h)-18; m = int(m)
        if problem1 in problem:
            count += 1
        problem.append(problem1)
        if status == 'AC':
            h,m = h+int((m+20*count)/60),(m + 20*count)%60
            if h < 10:
                penalty += '0'
            penalty += str(h)
            penalty += ':'
            if m < 10:
                penalty += '0'
            penalty += str(m)
            count = 0
    print(penalty)