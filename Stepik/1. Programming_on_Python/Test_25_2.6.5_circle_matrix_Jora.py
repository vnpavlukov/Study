def index(num, s):
    p = (s - 1)*4

    if s == 1:
        return 0, 0
    elif num < p:
        min_d = lambda x: 0
        max_d = lambda x: s-1
        top_j = lambda x: x
        right_i = lambda x: x-(s-1)
        bottom_j = lambda x: 3*(s-1)-x
        left_i = lambda x: 4*(s-1)-x

        i = [min_d, right_i, max_d, left_i][num//(s-1)](num)
        j = [top_j, max_d, bottom_j, min_d][num//(s-1)](num)
        return i, j
    else:
        i, j = index(num - p, s - 2)
        return i+1, j+1

def spiral(n):
    res = [[0 for col in range(n)] for row in range(n)]
    for num in range(n*n):
        i, j = index(num, n)
        res[i][j] = num + 1
    return res

for i in range(11):
    sp = spiral(i)
    for row in range(i):
        print(" ".join("{:3d}".format(x) for x in sp[row]))
    print()