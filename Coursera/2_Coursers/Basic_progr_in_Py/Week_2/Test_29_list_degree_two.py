limitation = int(input())


def find_list_degree_two(lim):
    max_num = 1
    print(max_num, end=' ')
    while max_num * 2 <= lim:
        max_num = max_num * 2
        print(max_num, end=' ')


find_list_degree_two(limitation)
