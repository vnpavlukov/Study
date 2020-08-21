number = int(input())


def circle_numbers(size):
    matrix = [[0 for x in range(size)] for y in range(size)]

    num = 1
    i = 0

    while size > 0:
        for right in range(size - 1):
            matrix[0 + i][right + i] = num
            num += 1

        for down in range(size - 1):
            matrix[down + i][-1 - i] = num
            num += 1

        for left in range(size - 1, 0, -1):
            matrix[-1 - i][left + i] = num
            num += 1

        for up in range(size - 1, 0, -1):
            matrix[up + i][0 + i] = num
            num += 1
        size -= 2
        i += 1

    if size == -1:
        matrix[i - 1][i - 1] = num

    return matrix


for i in circle_numbers(number):
    for p in i:
        print(p, end=' ')
    print()
