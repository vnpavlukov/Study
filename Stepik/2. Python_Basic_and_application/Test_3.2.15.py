input_string, find, replace = [input() for i in range(3)]
count_iteration = 0

while find in input_string:
    input_string = input_string.replace(find, replace)
    count_iteration += 1
    if count_iteration > 1000:
        count_iteration = 'Impossible'
        break

print(count_iteration)
