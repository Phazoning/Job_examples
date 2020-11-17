def squarediff(number):
    def multip(digit, list):
        sum = 0
        for e in list:
            if e != digit:
                sum += digit*e
        return sum

    sum = 0
    targets = []
    for e in range(number + 1):
        targets.append(e)
    for e in targets:
        sum += multip(e, targets)

    print(sum)

squarediff(100)