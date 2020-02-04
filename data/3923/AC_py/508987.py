# coding=utf-8
a=input()
while a!="":
    l=[]
    score=0
    q=0
    d=0
    u=0
    while q!=-1:
          q=a.find("1Y",q)
          if q!=-1:
              score=score+1
              q=q+2
    while d!=-1:
          d=a.find("2Y",d)
          if d!=-1:
              score=score+2
              d=d+2
    while u!=-1:
          u=a.find("3Y",u)
          if u!=-1:
              score=score+3
              u=u+2
        
    for i in a:
        l.append(i)
    r=l.count("R")
    a=l.count("A")
    s=l.count('S')
    b=l.count("B")
    t=l.count('T')
    shot=l.count("N")
    print(score+r+a+s+b-t-shot)

          
    a=input()