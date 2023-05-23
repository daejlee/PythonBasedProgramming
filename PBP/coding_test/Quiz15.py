import math as m

def get_maxdiv(a, b):
    ret = 1
    small = a if a < b else b
    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0:
            ret = i
    return ret


def get_minmultiple(a, b):
    ret = a if a > b else b
    small = a if a < b else b
    i = 1
    while True:
        if ret * i % small == 0:
            return ret * i
        i += 1

#삼항연산자 small = a if a < b else b