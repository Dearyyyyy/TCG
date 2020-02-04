import os
import FL.util as util
import FL.RealWorldLabGranularity.GSBFL.GSBFL as GSBFL
import FL.RealWorldLabGranularity.GMBFL.GMBFL as GMBFL
import sys


def savemethod(granularity, logFilePath, method, sus_oc, sus_tu, sus_op, sus_ds, sus_jac):
    util.save_result_with_granularity(granularity, logFilePath, method, sus_jac, "Jacard")
    util.save_result_with_granularity(granularity, logFilePath, method, sus_tu, "Tarantula")
    util.save_result_with_granularity(granularity, logFilePath, method, sus_oc, "Ochiai")
    util.save_result_with_granularity(granularity, logFilePath, method, sus_op, "Op2")
    util.save_result_with_granularity(granularity, logFilePath, method, sus_ds, "Dstar")


def GSBFLOP(granularity, logFilePath, src, testDataDir):
    lineNum, sus_oc, sus_tu, sus_op, sus_ds, sus_jac = GSBFL.work(granularity, src, testDataDir)
    savemethod(granularity, logFilePath, 'SBFL', sus_oc, sus_tu, sus_op, sus_ds, sus_jac)


def GMBFLOP(granularity, logFilePath, src, testDataDir):
    lineMax, sus_jac, sus_oc, sus_op, sus_tu, sus_ds = GMBFL.work(granularity, src, testDataDir)
    savemethod(granularity, logFilePath, 'MBFL', sus_oc, sus_tu, sus_op, sus_ds, sus_jac)


def work(logFilePath, src, testDataDir):
    for granularity in range(1, 11):
        GSBFLOP(granularity, logFilePath, src, testDataDir)
        GMBFLOP(granularity, logFilePath, src, testDataDir)


if __name__ == "__main__":
    src = "../data/3919/WA_py/508113.py"
    testDataDir = "../data/3919/TEST_DATA_SPLIT"

    work("1", src, testDataDir)
