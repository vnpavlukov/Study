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
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()