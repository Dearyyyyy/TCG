# coding=utf-8
while True:
    n = int(input())
    problem = ''
    count = []
    for i in range(n):
        time, problem1, status = input().split()
        h = int(time[:2])-18
        m = int(time[3:])
        if problem1 in problem:
            count[problem.find(problem1)] += 1
        else:
            count.append(0)
            problem += problem1
        if status == 'AC':
            hour, minute = h+int((m+20*count[problem.find(problem1)])/60), (m+20*count[problem.find(problem1)])%60
    print("%02d:%02d"%(hour,minute))