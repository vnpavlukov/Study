line_1 = int(input())
line_2 = int(input())
line_3 = int(input())

# line_1 = 3
# line_2 = 2
# line_3 = 1

my_lines = [line_1, line_2, line_3]
my_lines.sort()


def type_of_tri(short_1, short_2, long):
    if long >= short_1 + short_2:
        return "impossible"
    elif long ** 2 < short_1 ** 2 + short_2 ** 2:
        return "acute"
    elif long ** 2 == short_1 ** 2 + short_2 ** 2:
        return "rectangular"
    elif long ** 2 > short_1 ** 2 + short_2 ** 2:
        return "obtuse"


print(type_of_tri(my_lines[0], my_lines[1], my_lines[2]))
