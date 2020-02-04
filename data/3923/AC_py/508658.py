# coding=utf-8
while(True):
     
     
    s = input()
    shots = s.count('2') + s.count('3')
     
    score = s.count('1Y') + 2*s.count('2Y') + 3*s.count('3Y')
    hits = s.count('2Y') + s.count('3Y')
    throws = s.count('1')
    OKthrows = s.count('1Y')
    rebound = s.count('R')
    assists = s.count('A')
     
    steal = s.count('S')
    block = s.count('B')
    turnovers = s.count('T')
    value =  (score + rebound + assists + steal + block) - (shots - hits) - (throws - OKthrows) - turnovers
    print(value)