import py_compile
import pickle
import os


def save_result(logFilePath, method, sus, formular_name):
    methodDir = os.path.join("SusResult", method)
    tempfile = os.path.join(methodDir, logFilePath + ".txt")
    lineNum = len(sus)
    f = open(tempfile, 'a+', encoding='utf-8')
    f.write(formular_name)
    for index in range(1, lineNum + 1):
        f.write(" " + str(sus[index]))
    f.write("\n")
    f.close()


def save_result_with_proid(proid, logFilePath, method, sus, formular_name):
    methodDir = os.path.join("SusResult", method)
    proDir = os.path.join(methodDir, str(proid))
    ok = os.path.exists(proDir)
    if not ok:
        os.makedirs(proDir)

    tempfile = os.path.join(proDir, logFilePath + ".txt")
    lineNum = len(sus)
    f = open(tempfile, 'a+', encoding='utf-8')
    f.write(formular_name)
    for index in range(1, lineNum + 1):
        f.write(" " + str(sus[index]))
    f.write("\n")
    f.close()


def save_result_with_granularity(granularity, logFilePath, method, sus, formular_name):
    methodDir = os.path.join("SusResult", method)
    granularityDir = os.path.join(methodDir, str(granularity))
    ok = os.path.exists(granularityDir)
    if not ok:
        os.makedirs(granularityDir)
    tempfile = os.path.join(granularityDir, logFilePath + ".txt")

    lineNum = len(sus)
    f = open(tempfile, 'a+', encoding='utf-8')
    f.write(formular_name)
    for index in range(1, lineNum + 1):
        f.write(" " + str(sus[index]))
    f.write("\n")
    f.close()


def write_file(file_name, list):
    try:
        f = open(file_name, 'w', encoding='utf-8')
        f.writelines([line + '\n' for line in list])
        f.close()
    except:
        print("写入" + file_name + "出错")


def write_file_add(file_name, list):
    try:
        f = open(file_name, 'a+', encoding='utf-8')
        f.writelines([line + '\n' for line in list])
        f.close()
    except:
        print("写入" + file_name + "出错")


def compare_res(user_res, correct_res):
    user_res_text = read_line(user_res)
    correct_res_text = read_line(correct_res)
    flag = True

    if len(user_res_text) != len(correct_res_text):
        flag = False
    if flag:
        for i in range(len(correct_res_text)):
            if user_res_text[i] != correct_res_text[i]:
                flag = False
    return flag


def read_line(file_name):
    try:
        f = open(file_name, 'r', encoding='utf-8')
        text = f.read().splitlines()
        f.close()
        return text
    except:
        print("读取" + file_name + "出错")


def CheckCompile(file):
    data = py_compile.compile(file)
    if data:
        return True
    else:
        print("编译错误")
        return False


def logInfo(path, content):
    logfile = path
    f = open(logfile, 'a+', encoding='utf-8')
    f.write(content + "\n")
    f.close()


def OverWrite(path, content):
    logfile = path
    f = open(logfile, 'w', encoding='utf-8')
    f.write(content + "\n")
    f.close()


def mergeList(list1, list2):
    for item in list2:
        if item not in list1:
            list1.append(item)
    return list1

def mergeResult(res1, res2):
    return res1 and res2
