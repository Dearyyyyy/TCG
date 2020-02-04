import os
import sys
import datetime
import FL.MBFL.MBFL_Formular as MBFL_Formular
import FL.global_variable
import FL.util as util

if sys.platform == "linux":
    COMLINE_COV = "timeout 5 coverage run %s<%s"
    COMLINE_RUN = "timeout 5 python3 %s <%s >%s"
else:
    COMLINE_COV = "coverage run %s<%s"
    COMLINE_RUN = "python %s <%s >%s "


def getSrcCov(granularity, srcPath, testDataPathDir, outputDir):
    cov_info = []
    res = []
    file_order = []
    files = os.listdir(testDataPathDir)
    files.sort()
    for i in files:
        if ".in" not in i:
            continue
        input_file = os.path.join(testDataPathDir, i)
        output_file = os.path.join(testDataPathDir, i[: -2] + "out")
        file_order.append(i[: -2] + "out")
        cmd = COMLINE_COV % (srcPath, input_file)
        try:
            os.system(cmd)
            filename = ".coverage"
            f = open(filename, 'r')
            text = f.read()
            f.close()
            # print(text)
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

        try:
            outFIleName = os.path.join(outputDir, i[: -2] + "out")
            cmd = COMLINE_RUN % (srcPath, input_file, outFIleName)
            os.system(cmd)
            filename = outFIleName
            res.append(util.compare_res(filename, output_file))
        except:
            res.append(False)

    granularity_cov_info = []
    granularity_res = []
    mod = len(res)
    for i in range(10):
        stpos = i * granularity
        edpos = (i + 1) * granularity
        temp_cov = []
        temp_res = True
        for index in range(stpos, edpos):
            temp_cov = util.mergeList(temp_cov, cov_info[index % mod])
            temp_res = util.mergeResult(temp_res, res[index % mod])
        granularity_cov_info.append(temp_cov)
        granularity_res.append(temp_res)
    return granularity_cov_info, granularity_res, file_order

def getInfo(granularity, temp_order, caseNum, res, mutateOutPutDir, programOutPutDir):
    Akf, Anf, Akp, Anp = 0, 0, 0, 0
    mod = len(temp_order)
    for i in range(caseNum):
        stpos = i * granularity
        edpos = (i + 1) * granularity
        kill = True
        for index in range(stpos, edpos):
            myOutFile = os.path.join(programOutPutDir, temp_order[index%mod])
            mutantOutFile = os.path.join(mutateOutPutDir, temp_order[index%mod])
            kill = util.mergeResult(kill, not util.compare_res(mutantOutFile, myOutFile))

        if res[i] == True:
            if kill == True:
                Akp += 1
            if kill == False:
                Anp += 1
        if res[i] == False:
            if kill == True:
                Akf += 1
            if kill == False:
                Anf += 1
    return Akf, Anf, Akp, Anp


def work(granularity, pyFilePath, testDataDirPath):
    src = pyFilePath
    testDataPath = testDataDirPath
    mutatePath = './mutant/mutant.py'
    mutateOutPutDir = './mutant_output'
    programOutPutDir = './program_output'
    cov, res, order = getSrcCov(granularity, src, testDataPath, programOutPutDir)
    caseNum = len(res)
    list = util.read_line(src)
    lineMax = len(list)
    mutantcnt = 0
    sus_jac = {}
    sus_oc = {}
    sus_op = {}
    sus_tu = {}
    sus_ds = {}
    vis = {}
    for i in range(1, lineMax + 1):
        sus_jac[i] = 0
        sus_oc[i] = 0
        sus_op[i] = 0
        sus_tu[i] = 0
        sus_ds[i] = 0
        vis[i] = 0
    for i in range(caseNum):
        if res[i] == False:
            for lineIndex in cov[i]:
                if vis[lineIndex] == 1:
                    continue
                vis[lineIndex] = 1
                line = list[lineIndex - 1]
                temp_sus_jac = [0]
                temp_sus_oc = [0]
                temp_sus_op = [0]
                temp_sus_tu = [0]
                temp_sus_ds = [0]
                for key, value in MBFL_Formular.mutation_trick.items():
                    if "#" in line:
                        continue
                    if key in line:
                        for mutation_operator in value:
                            linelen = len(line)
                            pos = 0
                            while pos >= 0 and pos < linelen:
                                pos = line.find(key, pos)
                                if pos == -1:
                                    break
                                newline = line[0:pos] + mutation_operator + line[pos + len(key):]
                                pos += len(key)
                                newlist = list[:]
                                newlist[lineIndex - 1] = newline
                                util.write_file(mutatePath, newlist)
                                if util.CheckCompile(mutatePath):
                                    mutantcnt += 1
                                else:
                                    continue
                                starttime = datetime.datetime.now()
                                temp_cov, temp_res, temp_order = getSrcCov(granularity, mutatePath, testDataPath,
                                                                           mutateOutPutDir)
                                Akf, Anf, Akp, Anp = getInfo(granularity, temp_order, caseNum, res, mutateOutPutDir,
                                                             programOutPutDir)
                                endtime = datetime.datetime.now()
                                logcontent = "%d行%d位置从%s变异到%s %d %d %d %d %s执行%d变异体所耗时间%f" % (
                                    lineIndex, pos, key, mutation_operator, Akf, Anf, Akp, Anp, src, mutantcnt,
                                    (endtime - starttime).seconds)
                                util.logInfo("./REAL_MutantTime.txt", logcontent)

                                temp_sus_jac.append(MBFL_Formular.cal_jaccard(Akf, Anf, Akp, Anp))
                                temp_sus_oc.append(MBFL_Formular.cal_ochiai(Akf, Anf, Akp, Anp))
                                temp_sus_op.append(MBFL_Formular.cal_op2(Akf, Anf, Akp, Anp))
                                temp_sus_tu.append(MBFL_Formular.cal_tarantula(Akf, Anf, Akp, Anp))
                                temp_sus_ds.append(MBFL_Formular.cal_dstar(Akf, Anf, Akp, Anp, 3))
                sus_jac[lineIndex] = max(sus_jac[lineIndex], max(temp_sus_jac))
                sus_oc[lineIndex] = max(sus_oc[lineIndex], max(temp_sus_oc))
                sus_op[lineIndex] = max(sus_op[lineIndex], max(temp_sus_op))
                sus_ds[lineIndex] = max(sus_ds[lineIndex], max(temp_sus_ds))
                sus_tu[lineIndex] = max(sus_tu[lineIndex], max(temp_sus_tu))
    return lineMax, sus_jac, sus_oc, sus_op, sus_tu, sus_ds


if __name__ == '__main__':
    a = 1
