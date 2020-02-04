# coding=utf-8
s = input("")
if not s :
    print("")
    s = input("")
 
rs = list(reversed(s))
if list(s) == rs:
    print("YES")
else:
    print("NO")