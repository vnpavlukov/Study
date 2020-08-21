l_1 = int(input())
r_1 = int(input())
l_2 = int(input())
r_2 = int(input())
l_3 = int(input())
r_3 = int(input())
# l_1 = 1
# r_1 = 26
# l_2 = 51
# r_2 = 52
# l_3 = 79
# r_3 = 81

Line_1, Line_2, Line_3 = (l_1, r_1), (l_2, r_2), (l_3, r_3)


def distance(line_1, line_2):
    sort_l = [line_1, line_2]
    sort_l.sort()
    return sort_l[1][0] - sort_l[0][1]


def len_line(line): return line[1] - line[0]


def contact_match(line_1, line_2, line_3):
    sort_lines = [line_1, line_2, line_3]
    sort_lines.sort()

    if distance(sort_lines[0], sort_lines[1]) <= 0 and \
            (distance(sort_lines[0], sort_lines[2]) <= 0 or
             distance(sort_lines[1], sort_lines[2]) <= 0):
        return 0  # no need to move

    if distance(line_2, line_3) <= len_line(line_1):
        return 1
    elif distance(line_1, line_3) <= len_line(line_2):
        return 2
    elif distance(line_1, line_2) <= len_line(line_3):
        return 3

    if distance(sort_lines[0], sort_lines[1]) > len_line(sort_lines[2]):
        return -1  # moving won't help


print(contact_match(Line_1, Line_2, Line_3))
