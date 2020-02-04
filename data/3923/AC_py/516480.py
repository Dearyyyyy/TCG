# coding=utf-8
while True:
    s=input()
    for i in range(len(s)):
     x=s.count("R")+s.count("A")+s.count("S")+s.count("B")+s.count("1Y")+2*s.count("2Y")+3*s.count("3Y")
     y=s.count("2N")+s.count("3N")
     z=s.count("1N")
     t=s.count("T")
    print(x-y-z-t)