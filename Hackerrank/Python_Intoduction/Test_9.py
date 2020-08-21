def average_rating(data, student):
    return sum(data[student]) / len(data[student])


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print('{:.2f}'.format(average_rating(student_marks, query_name)))
