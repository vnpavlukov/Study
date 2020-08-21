data = []
with open("Test_33_3.4.3_academic_performance.txt", "r",
          encoding='utf-8') as file_in:
    for line in file_in:
        c = []
        for i in line.strip().split(';'):
            c.append(i)
        data.append(c)

for rating in data:
    print((int(rating[1]) + int(rating[2]) + int(rating[3])) / 3)


def average_rating(in_data, xxx):
    count, x = 0, 0
    for math_rating in in_data:
        x += int(math_rating[xxx])
        count += 1
    return x / count


print(average_rating(data, 1),
      average_rating(data, 2),
      average_rating(data, 3))
