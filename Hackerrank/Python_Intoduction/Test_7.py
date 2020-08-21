def find_second_max(array):
    res = []
    for i in array:
        if i not in res:
            res.append(i)
    return sorted(res)[1]


def print_second_score_student(data, second_score):
    for key, value in sorted(data.items()):
        if value == second_score:
            print(key)


if __name__ == '__main__':
    arr = []
    rating = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        rating[name] = score
        arr.append(score)
    print_second_score_student(rating, find_second_max(arr))
