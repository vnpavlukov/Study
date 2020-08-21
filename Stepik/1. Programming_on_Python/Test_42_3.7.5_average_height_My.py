with open("Test_42_3.7.5_average_height.tsv", "r",
          encoding='utf-8') as file_in:
    data = []
    for line in file_in:
        c = []
        for i in line.strip().split('\t'):
            c.append(i)
        data.append(c)

count_students = [0 for i in range(12)]
sum_if_height = [0 for i in range(12)]
average_height = [0 for i in range(12)]

for row in data:
    in_class = int(row[0])
    count_students[in_class] += 1
    sum_if_height[in_class] += float(row[2])

for i in range(12):
    if count_students[i] == 0:
        average_height[i] = None
    else:
        average_height[i] = sum_if_height[i] / count_students[i]

for i in range(1, 12):
    print(i, '', end='')
    if average_height[i] == None:
        print('-')
    else:
        print(average_height[i])
