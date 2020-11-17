def fibo_sum(number):
    def fibon(first, second):
        fst = first
        snd = second
        next = False
        ret = [fst, second]
        while next < number:
            next = fst + snd
            fst = snd
            snd = next
            if next < number:
                ret.append(next)
        return ret

    fib = fibon(1, 2)
    ret = 0
    for e in fib:
        if e%2 == 0:
            ret += e
    print(ret)
    return ret

fibo_sum(4000000)