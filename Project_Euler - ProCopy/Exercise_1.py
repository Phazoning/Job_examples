def find(number):
    def findmult(alternumber):
        ret = []
        for e in range(number):
            if e % alternumber == 0:
                ret.append(e)
        return ret
    li = []
    li.extend(findmult(3))
    li.extend(findmult(5))
    used = []
    ret = 0
    for e in li:
        if used.count(e) < 1:
            used.append(e)
            ret += e
    print(ret)
    return ret