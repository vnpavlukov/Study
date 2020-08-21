def checkSymmetrySimple(num):
    a = num // 1000
    b = num % 1000 // 100
    c = num % 100 // 10
    d = num % 10
    return int(a == d and b == c)


def checkSymmetry(num):
    a = num // 1000
    b = num % 1000 // 100
    c = num % 100 // 10
    d = num % 10
    symmetry = ((a + 1) / (d + 1) + (b + 1) / (c + 1) - 1) % 2
    return int(symmetry)


for i in range(9999):
    if checkSymmetrySimple(i) == checkSymmetry(i):
        print(i)