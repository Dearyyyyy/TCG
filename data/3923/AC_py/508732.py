# coding=utf-8
while True:
    try:
        a=input()
        str1="1Y"
        str2="1N"
        str3="2Y"
        str4="2N"
        str5="3Y"
        str6="3N"
        num1=(len(a)-len(a.replace(str1,"")))/2+(len(a)-len(a.replace(str3,"")))+(len(a)-len(a.replace(str5,"")))*3/2
        num2=(len(a)-len(a.replace("R","")))
        num3=(len(a)-len(a.replace("A","")))
        num4=(len(a)-len(a.replace("S","")))
        num5=(len(a)-len(a.replace("B","")))
        num6=(len(a)-len(a.replace("T","")))
        num7=(len(a)-len(a.replace(str4,"")))/2+(len(a)-len(a.replace(str3,"")))/2+(len(a)-len(a.replace(str5,"")))/2+(len(a)-len(a.replace(str6,"")))/2
        num8=(len(a)-len(a.replace(str3,"")))/2+(len(a)-len(a.replace(str5,"")))/2
        num9=(len(a)-len(a.replace(str1,"")))/2+(len(a)-len(a.replace(str2,"")))/2
        num10=(len(a)-len(a.replace(str1,"")))/2        
        value=(num1+num2+num3+num4+num5)-(num7-num8)-(num9-num10)-num6
        print("%d"%value)
    except:
        break