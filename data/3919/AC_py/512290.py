# coding=utf-8
# 判断三角形
def triangle_judge(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    if not (x+y>z and x+z>y and z+y>x): # 两边之和大于第三边
        return 'ERROR'
    elif x==y==z:
        return 'DB'
    elif x==y or y==z or x==z:
        return 'DY'
    elif x*x+y*y==z*z or x*x+z*z==y*y or y*y+z*z==x*x:
        return 'ZJ'
    else:
        return 'PT'

def main():
    data1 = input()
    x1, y1, z1 = data1.split(' ')
    print(triangle_judge(x1, y1, z1))
    
    
if __name__ == '__main__':
    for i in range(3):
        main()