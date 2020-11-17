from math import sqrt as rt

def pyth_seq(number):
    def stifel(nu):
        a = (2*nu + 3)
        b = (nu + 1)*a + (nu + 1)
        c = int(rt(a**2 + b**2))
        return [a, b, c]

    def ozanam(nu):
        a = 4*nu + 8
        b = (nu + 1)*a + 4*nu + 7
        c = int(rt(a**2 + b**2))
        return [a, b, c]
    n = 0
    tp = []
    while tp == []:

        sti = stifel(n)
        oza = ozanam(n)
        stisum = 0
        ozasum = 0

        for e in sti:
            stisum += e
        for e in oza:
            ozasum += e

        if stisum == number:
            tp = sti
        elif ozasum == number:
            tp = oza
        elif number % stisum == 0:
            mul = number // stisum
            for e in range(len(sti)):
                sti[e] = sti[e]*mul
                tp = sti
        elif number % ozasum == 0:
            mul = number // ozasum
            for e in range(len(oza)):
                oza[e] = oza[e] * mul
                tp = oza
        else:
            n += 1

    print(tp)
    prod = 1
    for e in tp:
        prod *= e

    print(prod)


pyth_seq(1000)