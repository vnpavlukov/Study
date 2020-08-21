def create_matrix():
    matrix = []
    while True:
        numbers = input()
        if numbers == 'end':
            break
        matrix.append([int(i) for i in numbers.split()])
    return matrix


def refactor_matrix(input_m):
    rows = len(input_m)
    columns = len(input_m[0])
    out_m = [[0 for x in range(columns)] for y in range(rows)]

    for i in range(rows):
        for j in range(columns):
            out_m[i][j] = input_m[i][(j + 1) % columns] + \
                          input_m[(i + 1) % rows][j] + \
                          input_m[i][j - 1] + \
                          input_m[i - 1][j]
    return out_m


new_matrix = create_matrix()
ref_matrix = refactor_matrix(new_matrix)

for i in ref_matrix:
    for j in i:
        print(j, end=' ')
    print()
