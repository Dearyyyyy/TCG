# coding=utf-8

while True:
    n=input()
    n=int(n)
    problem=""
    count = []
    hour = []
    minute = []
    AC = []
    for i in range(n):
        time, problem1, status = input().split()
        if problem1 in problem:
            count[problem.find(problem1)]+=1
        else:
            count.append(0)
            problem=problem+problem1
        if status == 'AC' and problem1 not in AC:
            h=int(time[:2])-18
            m=int(time[3:])
            hour.append(h)
            minute.append(m + 20 * count[problem.find(problem1)])
            AC.append(problem1)
    sum1 = 0
    for i in minute:
        sum1 += i
    sum2 = 0
    for j in hour:
        sum2 += j
    sum2, sum1 = sum2 + int(sum1 / 60), sum1 % 60
    print("{:02d}:{:02d}".format(sum2,sum1))