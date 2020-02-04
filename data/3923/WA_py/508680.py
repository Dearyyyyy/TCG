# coding=utf-8
s=input()
while s:
    i=0
    efficiency_value = 0 
    score = 0
    rebound = 0
    assists = 0 
    steal = 0
    block = 0 
    shots = 0
    hits = 0 
    free_throws = 0
    successful_free_throws = 0
    turnovers = 0 
    while i<len(s):
        
        if s[i]=="1":
            if s[i+1]=="Y":
                score += 1
                free_throws += 1 
                successful_free_throws += 1 
                i += 1
            else:
                free_throws += 1 
                i += 1
        elif s[i]=="2":
            if s[i+1]=="Y":
                score += 2
                shots += 1 
                hits += 1 
                i += 1
            else:
                shots += 1 
                i += 1
        elif s[i]=="3":
            if s[i+1]=="Y":
                score += 3
                shots += 1 
                hits += 1 
                i += 1
            else:
                shots += 1 
                i += 1 
        elif s[i]=="R":
            
            rebound += 1 
            i += 1 
        elif s[i]=="A":
            
            assists += 1 
            i += 1 
        elif s[i]=="B":
            
            block += 1 
            i += 1 
        elif s[i]=="S":
          
            steal += 1 
            i += 1  
        elif s[i]=="T:
            turnovers += 1 
            i += 1
    efficiency_value = score + rebound + assists + steal + block - (shots - hits) - (free_throws - successful_free_throws) - turnovers
    print(efficiency_value)
    s = input()