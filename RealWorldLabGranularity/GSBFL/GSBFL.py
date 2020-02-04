# coding=utf-8
import sys
import os
import codecs
import FL.SBFL.SBFL_Formular as SBFL_Formular
import FL.global_variable
import FL.util as util

if sys.platform == "linux":
    COMLINE_COV = "timeout 5 coverage run %s<%s"
    COMLINE_RUN = "timeout 5 python3 %s <%s >%s "
else:
    COMLINE_COV = "coverage run %s<%s"
    COMLINE_RUN = "python %s <%s >%s "


def getSrcCov(granularity, srcPath, testDataPathDir):
    cov_info = []
    res = []
    files = os.listdir(testDataPathDir)
    for i in files:
        if ".in" not in i:
            continue
        input_file = os.path.join(testDataPathDir, i)
        output_file = os.path.join(testDataPathDir, i[: -2] + "out")
        cmd = COMLINE_COV % (srcPath, input_file)

        try:
            os.system(cmd)
            filename = ".coverage"
            f = open(filename, 'r')
            text = f.read()
            f.close()
            posr = text.rfind(']')
            posl = text.rfind('[')
            sub = text[posl + 1:posr].split(',')
            subs = []
            for item in sub:
                subs.append(int(item))
                subs.sort()
            cov_info.append(subs)
        except:
            cov_info.append([])

        cmd = COMLINE_RUN % (srcPath, input_file, './temp.out')
        os.system(cmd)
        filename = "./temp.out"
        res.append(util.compare_res(filename, output_file))

    granularity_cov_info = []
    granularity_res = []
    mod = len(res)
    for i in range(10):
        stpos = i*granularity
        edpos = (i+1)*granularity
        temp_cov = []
        temp_res = True
        for index in range(stpos,edpos+1):
            temp_cov = util.mergeList(temp_cov,cov_info[index%mod])
            temp_res = util.mergeResult(temp_res, res[index % mod])
        granularity_cov_info.append(temp_cov)
        granularity_res.append(temp_res)
    return granularity_cov_info, granularity_res

def CountInfo(lineMax, cov, res):
    caseNum = len(res)
    stateICovNum, stateICovPassNum, stateICovFailNum = {}, {}, {}
    stateIunCovNum, stateIunCovPassNum, stateIunCovFailNum = {}, {}, {}

    for lineIndex in range(1, lineMax + 1):
        covPass, covFail, uncovPass, uncovFail = 0, 0, 0, 0
        for caseIndex in range(0, caseNum):
            if lineIndex in cov[caseIndex]:
                if res[caseIndex] is True:
                    covPass += 1
                else:
                    covFail += 1
            else:
                if res[caseIndex] is True:
                    uncovPass += 1
                else:
                    uncovFail += 1
        stateICovNum[lineIndex] = covPass + covFail
        stateICovPassNum[lineIndex] = covPass
        stateICovFailNum[lineIndex] = covFail
        stateIunCovNum[lineIndex] = uncovPass + uncovFail
        stateIunCovPassNum[lineIndex] = uncovPass
        stateIunCovFailNum[lineIndex] = uncovFail

    return lineMax, caseNum, res.count(True), res.count(False) \
        , stateICovNum, stateICovPassNum, stateICovFailNum \
        , stateIunCovNum, stateIunCovPassNum, stateIunCovFailNum


def work(granularity, pyFilePath, testDataDirPath):
    src = pyFilePath
    testDataPath = testDataDirPath
    cov, res = getSrcCov(granularity, src, testDataPath)
    list = util.read_line(src)
    lineMax = len(list)
    lineNum, caseNum, casePass, caseFail, siCovCase, siCovPass, siCovFail, siunCovCase, siunCovPass, siunCovFail = CountInfo(
        lineMax,
        cov, res)
    sus_oc = {}
    sus_tu = {}
    sus_op = {}
    sus_ds = {}
    sus_jac = {}
    for lineIndex in range(1, lineNum + 1):
        sus_oc[lineIndex] = SBFL_Formular.cal_ochiai(caseFail, casePass, siCovFail[lineIndex], siCovPass[lineIndex],
                                                     siunCovFail[lineIndex], siunCovPass[lineIndex])
        sus_tu[lineIndex] = SBFL_Formular.cal_turantula(caseFail, casePass, siCovFail[lineIndex], siCovPass[lineIndex],
                                                        siunCovFail[lineIndex], siunCovPass[lineIndex])
        sus_op[lineIndex] = SBFL_Formular.cal_op2(caseFail, casePass, siCovFail[lineIndex], siCovPass[lineIndex],
                                                  siunCovFail[lineIndex], siunCovPass[lineIndex])
        sus_ds[lineIndex] = SBFL_Formular.cal_dstar(caseFail, casePass, siCovFail[lineIndex], siCovPass[lineIndex],
                                                    siunCovFail[lineIndex], siunCovPass[lineIndex], 3)
        sus_jac[lineIndex] = SBFL_Formular.cal_jaccard(caseFail, casePass, siCovFail[lineIndex], siCovPass[lineIndex],
                                                       siunCovFail[lineIndex], siunCovPass[lineIndex])
    return lineNum, sus_oc, sus_tu, sus_op, sus_ds, sus_jac


if __name__ == '__main__':
    a = 1
