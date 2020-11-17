def nthprime(number):
    primes = [2, 3]
    n = 5
    while len(primes) < number:
        div = []
        m = 2
        while len(div) < 1:
            if n % m == 0:
                div.append(m)
            else:
                m += 1
        if div == [n]:
            primes.append(n)
        n += 1
    return primes[number - 1]
