# coding=utf-8
n=input()
n=int(n)
current_number = 1
while current_number < n :
    Len =len(string)
    string = input("请输入一个字符串")
    count = 0
    flag = 1
    while count < Len//2 :
        if string[count]!=string[Len-count-1] :
            flag = 0
            break
        count +=1
    if flag == 1 :
        print("Yes")
    else flag == 0 :
        print("No")
    i+=1