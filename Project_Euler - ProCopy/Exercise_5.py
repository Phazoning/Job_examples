def lesser_multiple(start, finish):
    def find_factors(nu):
        primes = []
        for e in range(2, nu + 1):
            fact = []
            n = 2
            while len(fact) < 1:
                if e % n == 0:
                    fact.append(n)
                n += 1
            if fact == [e]:
                primes.append(e)
        stor = nu
        fact = []
        n = 0
        while primes.count(stor) < 1:
            if stor % primes[n] == 0:
                fact.append(primes[n])
                stor //= primes[n]
                n = 0
            else:
                n += 1
        fact.append(stor)
        diff_facts = []
        for e in fact:
            if diff_facts.count(e) < 1:
                diff_facts.append(e)
        return [diff_facts, fact]

    facts = []
    for e in range(start, finish + 1):
        func_res = find_factors(e)
        factors = func_res[0]
        factoriz = func_res[1]
        for e in factors:
            difference = facts.count(e) - factoriz.count(e)
            if difference < 0:
                for j in range(abs(difference)):
                    facts.append(e)
    prod = 1
    for e in facts:
        prod *= e

    print(prod)






lesser_multiple(2, 20)