# coding=utf-8
import os
import sys
import shutil
import FL.util as util
import FL.RealWorldLabGranularity.FaultLocationGranularity as FaultLocation


def loadInitData():
    initdataPath = "../data/initdata.txt"
    res = util.read_line(initdataPath)
    return res


if __name__ == "__main__":
    initdata = loadInitData()
    for item in initdata:
        proId = item.split()[0]
        pyfilename = item.split()[1]
        logFilePath = proId + "_" + pyfilename[:-3]
        srcPath = os.path.join("../data", proId, "WA_py", pyfilename)
        testDataPath = os.path.join("../data", proId, "TEST_DATA_SPLIT")
        # print(logFilePath, srcPath, testDataPath)
        FaultLocation.work(logFilePath, srcPath, testDataPath)
