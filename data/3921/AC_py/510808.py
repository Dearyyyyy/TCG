# coding=utf-8
def fun():
    st=input()
    st1 = st[:: -1]
    if st == st1:
        print("YES")
    else:
        print("NO")
n=int(input())
for i in range(n):
    fun()