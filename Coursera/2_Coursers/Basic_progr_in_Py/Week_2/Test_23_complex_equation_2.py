f = int(input())
z = int(input())
c = int(input())
d = int(input())


def whole_solutions(a, b):
    if a == b == 0:
        return "INF"
    elif a == 0:
        return "NO"
    elif (-b / a).is_integer():
        return -b / a
    else:
        return "NO"


print(whole_solutions(f, z))
