def sum_of_num():
    n = int(input())
    if n == 0:
        return n
    else:
        return sum_of_num() + n


print(sum_of_num())
