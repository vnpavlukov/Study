def find_second_max(array):
    res = []
    for i in array:
        if i not in res:
            res.append(i)
    return sorted(res)[-2]


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(find_second_max(arr))
