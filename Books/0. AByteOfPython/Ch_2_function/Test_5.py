def total (i = 5, *numbers, ex_num):
    count = i
    for x in numbers:
        count += x
    count += ex_num
    print(count)

total(10, 1, 2, 4, ex_num=50)