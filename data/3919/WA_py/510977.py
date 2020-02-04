# coding=utf-8
def strlist2numlist(strlist,type = 'int'):
    """将字符列表转化为数值列表"""
    for i in range(len(strlist)):
        if type == 'int':
            try:
                int(strlist[i])
            except ValueError:
                pass
            else:
                strlist[i] = int(strlist[i])
        elif type == 'float':
            try:
                float(strlist[i])
            except ValueError:
                pass
            else:
                strlist[i] = float(strlist[i])
    return strlist

def right_triangle(edges):
    """判断是否为直角三角形"""
    flag = False
    for i in range(len(edges)):
        edges[i] = edges[i] ** 2
        
    for edge in edges:
        temp = edges[:]
        temp.remove(edge)
        if edge == sum(temp):
            flag = True
    return flag

triangle_edges_list = []
for i in range(2):
    temp_list = input().split()
    triangle_edges_list.append(strlist2numlist(temp_list))
    
for i in range(2):
    triangle_edges = triangle_edges_list[i]
    flag = 1
    for edge in triangle_edges:
        edges = triangle_edges[:]
        edges.remove(edge)
        if edge >= sum(edges):
            flag = 0
            
    if flag == 1:
        if len(set(triangle_edges)) == 1:
            print('DB')
        elif len(set(triangle_edges)) == 2:
            print('DY')
        elif right_triangle(triangle_edges):
            print('ZJ')
        else:
            print('PT')
    else:
        print('ERROR')