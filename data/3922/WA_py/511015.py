# coding=utf-8
num_str = '1'
num_list = []
while num_str:
    num_str = input()
    num_list.append(strl2numl(num_str.split()))
for nums in num_list:
    if nums:
        if nums[1] == 0:
            print('error')
        else:
            print(true_round(nums[0],nums[1]))