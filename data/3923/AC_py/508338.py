# coding=utf-8

while True:
    score = 0
    rebound = 0
    assists = 0
    steal = 0
    block = 0
    num_shot = 0
    num_hits = 0
    num_fthr = 0
    num_sthr = 0
    num_turn = 0
    Str = input()
    Str = str(Str)
    for i in range(len(Str)):
        if Str[i] == 'Y':
            sc = int(Str[i-1])
            if sc == 1:
                num_fthr += 1
                num_sthr += 1
                score += 1
            elif sc == 2:
                num_shot += 1
                num_hits += 1
                score += 2
            elif sc == 3:
                num_shot += 1
                num_hits += 1
                score += 3
        elif Str[i] == 'N':
            sc = int(Str[i - 1])
            if sc == 1:
                num_fthr += 1
            elif sc == 2:
                num_shot += 1
            elif sc == 3:
                num_shot += 1
        elif Str[i] == 'R':
            rebound += 1
        elif Str[i] == 'A':
            assists += 1
        elif Str[i] == 'S':
            steal += 1
        elif Str[i] == 'B':
            block += 1
        elif Str[i] == 'T':
            num_turn += 1
    ev = (score + rebound + assists + steal + block) - (num_shot - num_hits) -\
         (num_fthr - num_sthr) - num_turn
    print(ev)