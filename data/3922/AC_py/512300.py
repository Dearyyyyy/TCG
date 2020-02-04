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

def true_round(a,b):
    import math
    if a/b - math.floor(a/b) >= 0.5:
        return(math.ceil(a/b))
    else:
        return(math.floor(a/b))

        
N = 5
num_list = []
for i in range(N):
    nums = strl2numl(input().split())
    
    if nums[1] == 0:
        print('error')
    else:
        print(true_round(nums[0],nums[1]))