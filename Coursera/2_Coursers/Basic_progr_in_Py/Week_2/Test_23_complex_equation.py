a = int(input())
b = int(input())
c = int(input())
d = int(input())


# a = 0
# b = 0
# c = 1
# d = 1


def any_solution(a, b, c, d):
    if a == 0:
        return 'INF'

    x = -b / a

    if x % 1 != 0:
        return 'NO'
    elif c * x + d == 0:
        return 'NO'
    elif (a * x + b) / (c * x + d) == 0:
        return int(x)
    else:
        return 'NO'


print(any_solution(a, b, c, d))
