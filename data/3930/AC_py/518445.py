# coding=utf-8
t = int(input())
for i in range(t):
    n = int(input())
    
    res_list = [0,0,0,0,0,0,0]
    res_str = ''
    
    while n > 0:
        if  n >= 100:
            res_list[6] += 1
            n -= 100
        elif n >= 50:
            
            res_list[5] += 1
            n -= 50
        elif n >= 20:
            res_list[4] += 1
            n -=20
            
        elif n >= 10:
            res_list[3] += 1
            n -= 10
        elif n >= 5:
            res_list[2] += 1
            n -= 5
        elif n >= 2:
            res_list[1] += 1
            n -= 2
            
            
        else:
            res_list[0] += n
            n -= n
    for i in res_list:
        res_str += str(i)
        res_str += ' '
    print(res_str)