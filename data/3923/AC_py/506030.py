# coding=utf-8
while True:
    s = input()
    sLen = len(s)
    i = 0
    result = 0
    while i < sLen:
        if s[i] == 'R' or s[i] == 'S' or s[i] == 'B' or s[i] == 'A':
            result += 1
        elif s[i] == 'T':
            result -= 1
        elif s[i] == '1' or s[i] == '2' or s[i] == '3':
            if s[i + 1] == 'Y':
                result += int(s[i])
            else:
                result -= 1
            i += 1
        i += 1
    print(result)