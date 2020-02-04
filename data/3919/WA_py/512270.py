# coding=utf-8
def strl2numl(str_list, type_in='int'):
    """将字符列表转化为数值列表"""
    for i_in in range(len(str_list)):
        if type_in == 'int':
            try:
                int(str_list[i_in])
            except ValueError:
                pass
            else:
                str_list[i_in] = int(str_list[i_in])
        elif type_in == 'float':
            try:
                float(str_list[i_in])
            except ValueError:
                pass
            else:
                str_list[i_in] = float(str_list[i_in])
    return str_list


def right_triangle(edges_in):
    """判断是否为直角三角形"""
    flag_in = False
    for i_in in range(len(edges_in)):
        edges_in[i_in] = edges_in[i_in] ** 2

    for edge_in in edges_in:
        temp = edges_in[:]
        temp.remove(edge_in)
        if edge_in == sum(temp):
            flag_in = True
    return flag_in


def triangle_judgement(triangle_edges):
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
    elif flag == 0:
        print('ERROR')


if __name__ == '__main__':
    triangles = []
    for i in range(3):
        triangles.append(strl2numl(input().split()))
    for i in range(3):
        triangle_judgement(triangles[i])