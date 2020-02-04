# coding=utf-8
import sys


def rotate_str(a_string):
    list_str = list(a_string)
    str_last = list_str[0]
    list_str.append(str_last)
    list_str[0] = ''
    return ''.join(list_str)


if __name__ == '__main__':
    for str_line in sys.stdin:
        strings_list = str_line.split()
        flag = 0
        if len(strings_list[0]) == len(strings_list[1]):
            str_len = len(strings_list[0])
            for i in range(str_len):
                strings_list[0] = rotate_str(strings_list[0])
                if strings_list[0] == strings_list[1]:
                    flag = 1

        if flag == 1:
            print('Yes')
        else:
            print('No')