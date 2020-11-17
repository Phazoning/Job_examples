"""
a_2**b_2 == a_0*b_0

a_1*b_2 + a_2*b_1 == a_0*b_1 + b_0*a_1

a_0*b_2 + b_0*a_2 -> idpt.

"""

def largest_palyndrome():
    nums = []
    for e in range(999, 101, -1):
        for j in range(999, 101, -1):
            prod = e*j
            if nums.count(prod) < 1:
                nums.append(prod)
    nums.sort()
    ret = len(nums) - 1
    found = False
    while not found:
        z = list(str(nums[ret]))
        checks = []
        if len(z) % 2 != 0:
            z.pop(int(len(z)/2 + 0.5))

        for e in range(len(z) // 2):
            if z[e] == z[len(z) - e - 1]:
                checks.append(True)
        if checks.count(True) == len(z) // 2:
            found = True
        else:
            ret -= 1
    print(nums[ret])


largest_palyndrome()