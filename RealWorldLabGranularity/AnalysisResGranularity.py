import os
import FL.util as util

def getAVGRank(faultLine, suslist):
    rank = 1
    susValue = suslist[int(faultLine) - 1]
    newsusList = sorted(suslist, reverse=True)
    st = newsusList.index(susValue) + 1
    cnt = newsusList.count(susValue)
    # (st + st+cnt-1)/2
    rank = (st + st + cnt - 1) / 2
    return rank


def avg_rank(faultLine, dataFileName):
    dataList = util.read_line(dataFileName)
    res = {}
    res['totLine'] = len(dataList[0].split()) - 1
    for onelineinfo in dataList:
        suslist = onelineinfo.split()
        formular_name = suslist[0]
        suslist = list(map(float, suslist[1:]))
        res[formular_name] = getAVGRank(faultLine, suslist)
    return res


def checkTop(rank, x):
    if rank <= x:
        return 1
    return 0


def init():
    MBFLRES = {}
    SBFLRES = {}
    MBFLRES['totCnt'] = 0
    MBFLRES['totLine'] = 0

    SBFLRES['totCnt'] = 0
    SBFLRES['totLine'] = 0

    formularlist1 = ['Jacard', 'Tarantula', 'Ochiai', 'Op2', 'Dstar']
    ranktoplist = [1, 3, 5, 10]
    for formularname in formularlist1:
        MBFLRES[formularname] = {}
        SBFLRES[formularname] = {}
        MBFLRES[formularname]['EXAM'] = 0
        SBFLRES[formularname]['EXAM'] = 0
        MBFLRES[formularname]['EXAMper'] = 0
        SBFLRES[formularname]['EXAMper'] = 0
        for rank in ranktoplist:
            MBFLRES[formularname]['Top' + str(rank)] = 0
            SBFLRES[formularname]['Top' + str(rank)] = 0
            MBFLRES[formularname]['Top' + str(rank) + "per"] = 0
            SBFLRES[formularname]['Top' + str(rank) + "per"] = 0

    return MBFLRES, SBFLRES


def work(susDataDir, granularity):
    MBFLRES, SBFLRES = init()
    formularlist1 = ['Jacard', 'Tarantula', 'Ochiai', 'Op2', 'Dstar']
    ranktoplist = [1, 3, 5, 10]
    examMBFLsave = {'Jacard': [], 'Tarantula': [], 'Ochiai': [], 'Op2': [], 'Dstar': []}
    examSBFLsave = {'Jacard': [], 'Tarantula': [], 'Ochiai': [], 'Op2': [], 'Dstar': []}
    initdata = loadInitData()
    for item in initdata:
        proId = item.split()[0]
        pyfilename = item.split()[1]
        logFilePath = proId + "_" + pyfilename[:-3] + ".txt"
        faultLines = list(map(int, item[item.index("[") + 1:-1].split(",")))
        MBFLtempresList = []
        SBFLtempresList = []
        for faultLine in faultLines:
            MBFLtempresList.append(avg_rank(faultLine, os.path.join(susDataDir, "MBFL", granularity, logFilePath)))
            SBFLtempresList.append(avg_rank(faultLine, os.path.join(susDataDir, "SBFL", granularity, logFilePath)))
        MBFLtempres = MBFLtempresList[0]
        SBFLtempres = SBFLtempresList[0]
        for index in range(len(MBFLtempresList)):
            for formularname in formularlist1:
                MBFLtempres[formularname] = min(MBFLtempres[formularname], MBFLtempresList[index][formularname])
                SBFLtempres[formularname] = min(SBFLtempres[formularname], SBFLtempresList[index][formularname])

        MBFLRES['totCnt'] += 1
        MBFLRES['totLine'] += MBFLtempres['totLine']

        SBFLRES['totCnt'] += 1
        SBFLRES['totLine'] += SBFLtempres['totLine']

        for formularname in formularlist1:
            MBFLRES[formularname]['EXAM'] += MBFLtempres[formularname] / MBFLtempres['totLine']
            SBFLRES[formularname]['EXAM'] += SBFLtempres[formularname] / SBFLtempres['totLine']
            for rank in ranktoplist:
                MBFLRES[formularname]['Top' + str(rank)] += checkTop(MBFLtempres[formularname], rank)
                SBFLRES[formularname]['Top' + str(rank)] += checkTop(SBFLtempres[formularname], rank)

    for formularname in formularlist1:
        MBFLRES[formularname]['EXAMper'] = MBFLRES[formularname]['EXAM'] / MBFLRES['totCnt']
        SBFLRES[formularname]['EXAMper'] = SBFLRES[formularname]['EXAM'] / SBFLRES['totCnt']
        for rank in ranktoplist:
            MBFLRES[formularname]['Top' + str(rank) + "per"] = MBFLRES[formularname]['Top' + str(rank)] / MBFLRES[
                'totCnt']
            SBFLRES[formularname]['Top' + str(rank) + "per"] = SBFLRES[formularname]['Top' + str(rank)] / SBFLRES[
                'totCnt']

    content = ""
    for formularname in formularlist1:
        for rank in ranktoplist:
            content += "%d(%.1f%%)\t" % (
                SBFLRES[formularname]['Top' + str(rank)],
                round(SBFLRES[formularname]['Top' + str(rank) + "per"] * 100, 3))
        content += "%.3f" % SBFLRES[formularname]['EXAMper']
        content += "\n"
    for formularname in formularlist1:
        for rank in ranktoplist:
            content += "%d(%.1f%%)\t" % (
                MBFLRES[formularname]['Top' + str(rank)],
                round(MBFLRES[formularname]['Top' + str(rank) + "per"] * 100, 3))
        content += "%.3f" % MBFLRES[formularname]['EXAMper']
        content += "\n"

    util.write_file_add("./result.txt", ["G" + str(granularity)])
    # for formularname in formularlist1:
    #     util.write_file_add("./result.txt", ["MBFL-"+formularname])
    #     util.write_file_add("./result.txt",[str(examMBFLsave[formularname])])
    # for formularname in formularlist1:
    #     util.write_file_add("./result.txt", ["SBFL-" + formularname])
    #     util.write_file_add("./result.txt", [str(examSBFLsave[formularname])])
    util.write_file_add("./result.txt", [content])
    # print(SBFLRES)
    # print(MBFLRES)
    return


def loadInitData():
    initdataPath = "../data/initdata.txt"
    res = util.read_line(initdataPath)
    return res

def proinfomation():
    initdataPath = "../data/initdata.txt"
    res = util.read_line(initdataPath)

    countDic = {}
    for item in res:
        proId = int(item.split()[0])
        pyfilename = os.path.join("../data/",str(proId),"WA_py",item.split()[1])
        faultLines = list(map(int, item[item.index("[") + 1:-1].split(",")))
        if proId not in countDic.keys():
            countDic[proId] = {"Title":"","totalVersion": 0,"totalLines":0, "testcaseNum": 0, "maxLine": -1,
                               "minLine": 9999, "countFault": 0}
            testcasedir = os.path.join("../data/",str(proId),"TEST_DATA")
            testList = os.listdir(testcasedir)
            countDic[proId]["testcaseNum"] = len(testList)//2
        countDic[proId]["countFault"]+=len(faultLines)
        countDic[proId]["totalVersion"]+=1
        tempcontent = util.read_line(pyfilename)
        countDic[proId]["totalLines"]+=len(tempcontent)
        countDic[proId]["maxLine"] = max(countDic[proId]["maxLine"],len(tempcontent))
        countDic[proId]["minLine"] = min(countDic[proId]["minLine"], len(tempcontent))

    countDic[3919]["title"] = "Judge triangle"
    countDic[3921]["title"] = "Palindrome"
    countDic[3922]["title"] = "Division"
    countDic[3923]["title"] = "Basketball game"
    countDic[3930]["title"] = "Minimum currency payment problem"
    countDic[3943]["title"] = "Full Permutation"
    countDic[3955]["title"] = "Rotate string"

    countDic[3919]["description"] = "determine what kind of triangle it is based on the given three edges"
    countDic[3921]["description"] = "write a program to determine if the input string is a palindrome"
    countDic[3922]["description"] = "output the result of a/b, the result is rounded off, if b is equal to 0, then output error"
    countDic[3923]["description"] = "for each line of input, calulate the player's efficiency value"
    countDic[3930]["description"] = "calculate the minimum number of coins required to pay"
    countDic[3943]["description"] = "print the permutations of 1 to N are output in lexicographic order"
    countDic[3955]["description"] = "judge if the string A and string B are rotated string"


    for item in countDic.items():
        print(item)

if __name__ == "__main__":
    proinfomation()

    # susDataPath = "./SusResult"
    # for granularity in range(1, 11):
    #     work(susDataPath, str(granularity))
