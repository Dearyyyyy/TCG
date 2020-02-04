# coding=utf-8
q = int(input())
for i in range(q):
    y = int(input())
       
    res_list = [0,0,0,0,0,0,0]
    res_str = ''
       
    while y > 0:
        if  y >= 100:
            res_list[6] += 1
            y -= 100
        elif y >= 50:
               
            res_list[5] += 1
            y -= 50
        elif y >= 20:
            res_list[4] += 1
            y -=20
               
        elif y >= 10:
            res_list[3] += 1
            y -= 10
        elif y >= 5:
            res_list[2] += 1
            y -= 5
        elif y >= 2:
            res_list[1] += 1
            y -= 2
               
               
        else:
            res_list[0] += y
            y -= y
    for i in res_list:
        res_str += str(i)
        res_str += ' '
    print(res_str)