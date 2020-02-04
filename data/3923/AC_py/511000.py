# coding=utf-8
while(1):
    st = input()
    x = list(st)
    zf = 0
    k = len(st)
    fi = 0
    bi = 0
    fo = 0
    bo = 0
    for i in range(k):
        if x[i] == 'R' or x[i] == 'A' or x[i] == 'S' or x[i] == 'B':
            zf += 1
        elif x[i] == 'T':
            zf -= 1
        elif x[i] == 'Y':
            if x[i - 1] == '1':
                # fi += 1
                zf+=1
            else:
                # bi += 1
                p = int(x[i - 1])
                zf += p
        elif x[i] == 'N':
            if x[i - 1] == '1':
                fo -= 1
            else:
                bo -= 1
    print(zf + bo + fo)