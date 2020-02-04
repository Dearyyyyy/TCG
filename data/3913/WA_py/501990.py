# coding=utf-8


                
                

                
                
                
                
                    
                        line=[[0]*3]*3line2=[[0]*3]*3for i in range(3):    line[i]=input().split(" ")temp=line[0][1]line[0][1]=line[1][0]line[1][0]=temptemp=line[0][2]line[0][2]=line[2][0]line[2][0]=temptemp=line[1][2]line[1][2]=line[2][1]line[2][1]=tempfor i in range(3):    if i!=0:        print()    for j in range(3):        print(line[i][j],end=" ")