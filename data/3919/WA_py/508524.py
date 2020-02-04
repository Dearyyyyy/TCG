# coding=utf-8
# 。一名玩家得11分，另一名玩家得不到或等于9分。游戏结束，
# 前者获胜；2.
# 如果比分是10:10，那么比赛进入季后赛，两名球员轮
# 流发球。当差距为2分时，游戏结束，得分较高的玩家获胜。3.在
# 其他情况下，两名球员轮流发球两个球；
def sanjiao(a,b,c):
    if a == b and b ==c:
        print("DB")
    elif a==b or b == c or a ==c:
        print("DY")
    elif a*a +b*b == c*c or a*a +c*c == b*b or c*c +b*b == a*a:
        print('ZJ')
    elif a+b>c and c+b>a and c+a>b:
        print('PT')
    else :
        print('ERROR')
while True:
	a,b,c = input().split()
	a,b,c = int(a),int(b),int(c)
	sanjiao(a,b,c)