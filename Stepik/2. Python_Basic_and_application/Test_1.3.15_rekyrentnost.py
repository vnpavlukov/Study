a, b = map(int, input().split())


def count_combinations(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return count_combinations(n - 1, k) + count_combinations(n - 1, k - 1)


print(count_combinations(a, b))
