from Exercise_7 import nthprime as nth

def prime_sum(max_number=3):

    primer = [2, 3]
    chk = False

    n = 3
    while not chk:
        prime = nth(n)
        if max_number > prime:
            primer.append(prime)

            n += 1
        else:
            chk = True

    ret = 0
    for e in primer:
        ret += e

    print(ret)

prime_sum(2000000)