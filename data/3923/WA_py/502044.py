# coding=utf-8
while True:
    status=raw_input()
    score=status.count('1Y')+2*status.count('2Y')+3*status.count('3Y')
    rebound=status.count('R')
    asist=status.count('A')
    steal=status.count('S')
    block=status.count('B')
    attempt=status.count('2Y')+status.count('2N')+status.count('3Y')+status.count('3N')
    made=status.count('2Y')+status.count('3Y')
    ft_attempt=status.count('1Y')+status.count('1N')
    ft_made=status.count('1Y')
    turnover=status.count('T')
    e=((score+rebound+asist+steal+block)-(attempt-made)-(ft_attempt-ft_made)-turnover)
    print e