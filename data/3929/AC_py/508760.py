# coding=utf-8
while True:
    n = int(input())
    problem = ''
    hour = []
    count = []
    minute = []
    AC = []
    for i in range(n):
        time, problem1, status = input().split()
        h = int(time[:2])-18
        
        
        m = int(time[3:])
        if problem1 in problem:
            count[problem.find(problem1)] += 1
            
        else:
            count.append(0)
            problem += problem1
        if status == 'AC' and problem1 not in AC:
            hour.append(h+int((m+20*count[problem.find(problem1)])/60))
            minute.append((m+20*count[problem.find(problem1)]) % 60)
            AC.append(problem1)
    s1 = 0
    for i in minute:
        s1 += i
        
    s2 = 0
    for j in hour:
        s2 += j
    s2, s1 = s2+int(s1/60), s1 % 60
    print("%02d:%02d" % (s2, s1))