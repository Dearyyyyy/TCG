# coding=utf-8

while True:
    Q,W,E=input().split(" ")
    Q,W,E=int(Q),int(W),int(E)
    if Q+W>E and W+E>Q and Q+E>W:
        if Q==W and W==E and E==Q:
            print("DB")
        elif Q==W and W==E and E==Q:
            print("DY")
        elif Q*Q==W*W+E*E or W*W=Q*Q+E*E or E*E=Q*Q+W*W:
            print("ZJ")
        else:
            print("PT")
    else:
        print("ERROR")