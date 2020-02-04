# coding=utf-8
import sys


def time_minus(start_time, end_time):
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


for line in sys.stdin:
    if len(line) == 2:
        set_length = int(line)
        time_calculation = '00:00'
        wrong_time = '00:00'
        question = []
    else:
        data_line = line.split()
        if data_line[2] != 'AC':
            wrong_time = time_plus(wrong_time, '00:20')
        else:
            right_time = time_minus('18:00', data_line[0])
            time_calculation = time_plus(time_calculation, right_time)
            time_calculation = time_plus(time_calculation, wrong_time)
            wrong_time = '00:00'
            question.append(data_line[1])
        set_length -= 1
        if set_length == 0:
            print(time_calculation)