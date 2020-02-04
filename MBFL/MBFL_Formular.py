import math

debug = False
NULL_STRING = " "
mutation_trick = {
    ' not ': [' '],
    ' is ': [' is not '],
    ' in ': [' not in '],
    'break': ['continue'],
    'continue': ['break'],
    'True': ['False'],
    'False': ['True'],
    ' and ': [' or '],
    ' or ': [' and '],
    "<": ["!=", ">", "<=", ">=", "=="],
    ">": ["!=", "<", "<=", ">=", "=="],
    "<=": ["!=", "<", ">", ">=", "=="],
    ">=": ["!=", "<", "<=", ">", "=="],
    "==": ["!=", "=", "<", ">", "<=", ">="],
    "!=": ["==", "=", "<", ">", "<=", ">="],
    "+": ["-", "*", "/", "%", "//"],
    "-": ["+", "*", "/", "%", "//"],
    "*": ["+", "-", "/", "%", "//"],
    "/": ["%", "*", "+", "-", "//"],
    "%": ["/", "+", "-", "*", "//"],
    "//": ["/", "+", "-", "*", "%"],
    "**": ["/", "+", "-", "*", "%", "//"],
    "+ 1": ["- 1", "+ 0", "+ 2", "- 2"],
    "- 1": ["+ 1", "+ 0", "+ 2", "- 2"],
    "&": ["|", "^"],
    "|": ["&", "^"],
    "^": ["&", "|"],
    "~": [NULL_STRING],
    ">>": ["<<"],
    "<<": [">>"],
    "<<=": [">>=", "="],
    ">>=": [" <<=", "="],
}


# (fail/totfail)/((fail/totfail)+(pass/totpass))
# Akf = aef  Anf = anf
# totfail = Akf + Anf

def cal_tarantula(Akf, Anf, Akp, Anp):
    if Akf == 0:
        return 0
    if Akf + Anf == 0 or Akp + Anp == 0:
        return 0
    a = Akf / (Akf + Anf)
    b = Akp / (Akp + Anp)
    c = a / (a + b)
    return c


# (fail^index)/(pass+(totfail-fail))
def cal_dstar(Akf, Anf, Akp, Anp, index):
    a = Akp + (Akf + Anf - Akf)
    if a == 0:
        return 0
    b = math.pow(Akf, index)
    c = b / a
    return c


def cal_jaccard(Akf, Anf, Akp, Anp):
    if (Akf + Anf + Akp) == 0:
        return 0
    return Akf / (Akf + Anf + Akp)


def cal_ochiai(Akf, Anf, Akp, Anp):
    if (Akf + Anf) * (Akf + Akp) == 0:
        return 0
    return Akf / math.sqrt((Akf + Anf) * (Akf + Akp))


def cal_op2(Akf, Anf, Akp, Anp):
    if (Akp + Anp + 1) == 0:
        return 0
    return Akf - Akp / (Akp + Anp + 1)
