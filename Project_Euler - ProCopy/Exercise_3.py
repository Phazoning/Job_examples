def largest_factor(number):
    def isprime(nu):
        div = [1]
        while len(div) < 2:
            n = 2
            while nu % n != 0:
                n += 1
            div.append(n)
        if div == [1, nu]:
            return True
        else:
            return False
    tar = number
    nu = 2
    while not isprime(tar):
        while tar % nu != 0:
            nu += 1
        tar = tar // nu

    return tar
