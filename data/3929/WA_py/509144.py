# coding=utf-8
while True:
    n = int(input())
    count = []
    h = []
    m = []
    zm = []
    s = ''
    for i in range(n):
        time,s1,m = input().split()
        timelist = time.split(":")
        timelist = [int(x) for x in timelist]
        shi = timelist[0]
        fen = timelist[1]
        if s1 in s:
            count[s.find(s)]+=1
        else:
           count.append(0)
           s += s1
        if m=='AC' and s not in zm:
           h.append(shi+int((fen+20*count[pt.find(s)])/60))
           m.append((fen+20*count[pt.find(p)]%60))
           zm.append(s)
        shi = 0
        fen = 0
        for i in h:
            shi+=i
        for j in m:
            fen+=j
        shi,fen=shi+int(shi/60),fen%60
        print('%02d:%02d'%(shi,fen))