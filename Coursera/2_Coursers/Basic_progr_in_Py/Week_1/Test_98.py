answers = {
    1001:1,
    1000:0,
    1234:0,
    1221:1,
    220:1,
    20:0,
    0:1,
    1:0
}

def checkSymmetry(num):
    a = num // 1000
    b = num % 1000 // 100
    c = num % 100 // 10
    d = num % 10

    symmetry = (a + 1) / (d + 1) + (b + 1) / (c + 1) - 1
    return int(symmetry)


for key in answers:
    print(key, answers[key], checkSymmetry(key), answers[key] == checkSymmetry(key))