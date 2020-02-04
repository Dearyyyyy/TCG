# coding=utf-8
import sys


def time_minus(start_time, end_time):
    """时间的减法"""
    start_time = start_time.split(':')
    end_time = end_time.split(':')
    hour_part = int(end_time[0]) - int(start_time[0])
    if int(end_time[1]) >= int(start_time[1]):
        minute_part = int(end_time[1]) - int(start_time[1])
    else:
        hour_part -= 1
        minute_part = int(end_time[1]) + 60 - int(start_time[1])
    hour_part = str(hour_part)
    minute_part = str(minute_part)
    if len(hour_part) == 1:
        hour_part = '0' + hour_part
    if len(minute_part) == 1:
        minute_part = '0' + minute_part
    return hour_part + ':' + minute_part


def time_plus(first_time, second_time):
    """时间的加法"""
    first_time = first_time.split(':')
    second_time = second_time.split(':')
    hour_part = int(second_time[0]) + int(first_time[0])
    if int(second_time[1]) + int(first_time[1]) < 60:
        minute_part = int(second_time[1]) + int(first_time[1])
    else:
        hour_part += 1
        minute_part = int(second_time[1]) + int(first_time[1]) - 60
    hour_part = str(hour_part)
    minute_part = str(minute_part)
    if len(hour_part) == 1:
        hour_part = '0' + hour_part
    if len(minute_part) == 1:
        minute_part = '0' + minute_part
    return hour_part + ':' + minute_part


out_put = []
for line in sys.stdin: #标准输入
    try:   #判断输入是否化为整型
        int(line)
    except ValueError:
        flag = False
    else:
        flag = True

    if flag: #输入为整型
        set_length = int(line)
        wrong_time = []  # 各题目罚时存储列表
        time_calculation = []  # 各题目时间存储列表
        for i in range(26): #罚时与时间存储列表初始化
            time_calculation.append('00:00')
            wrong_time.append('00:00')
        question = []
    else: #进行罚时与完成时间的获取与存储
        data_line = line.split()
        if data_line[2] != 'AC':
            if data_line[1] not in question:
                question_index = ord(data_line[1]) - ord('A')
                wrong_time[question_index] = time_plus(wrong_time[question_index], '00:20')
        else:
            if data_line[1] not in question:
                right_time = time_minus('18:00', data_line[0])
                question_index = ord(data_line[1]) - ord('A')
                time_calculation[question_index] = time_plus(time_calculation[question_index], right_time)
                question.append(data_line[1])
        set_length -= 1
        if set_length == 0: #存储总罚时
            total_penalty_time = '00:00'
            total_AC_time = '00:00'
            for question_number in question:
                question_index = ord(question_number) - ord('A')
                total_penalty_time = time_plus(total_penalty_time,wrong_time[question_index])
                total_AC_time = time_plus(total_AC_time,time_calculation[question_index])
            out_put.append(time_plus(total_AC_time,total_penalty_time))
            print(time_plus(total_AC_time,total_penalty_time))
#for time_cal in out_put: #输出总罚时
#    print(time_cal)